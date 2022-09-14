from django_filters import rest_framework as filters
from rest_framework import generics

from batchs.models import Batch
from batchs.serializers import BatchDetailSerializer, BatchSerializer

from .permissions import IsOwner, SuperUserAuth


class BatchIsActiveFilter(filters.FilterSet):
    is_active = filters.BooleanFilter("is_active")

    class Meta:
        model = Batch
        fields = []


class BatchsView(generics.ListCreateAPIView):
    permission_classes = [IsOwner | SuperUserAuth]
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    lookup_field = "id"

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BatchIsActiveFilter

    def perform_create(self, serializer):
        zone = serializer.validated_data["zone"]
        qs = Batch.objects.filter(zone=zone)
        serializer.save(number_batch=len(qs))


class UpdateBatchsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner | SuperUserAuth]
    queryset = Batch.objects.all()
    serializer_class = BatchDetailSerializer
    lookup_field = "id"
