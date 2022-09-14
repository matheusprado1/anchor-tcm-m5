from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from batchs.models import Batch
from batchs.serializers import BatchDetailSerializer, BatchSerializer

from .permissions import IsOwner, SuperUserAuth


class BatchsView(generics.ListCreateAPIView):
    permission_classes = [IsOwner|SuperUserAuth]
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    lookup_field = "id"

    def perform_create(self, serializer):
        zone = serializer.validated_data["zone"]
        qs = Batch.objects.filter(zone=zone)
        serializer.save(number_batch=len(qs))


class UpdateBatchsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner|SuperUserAuth]
    queryset = Batch.objects.all()
    serializer_class = BatchDetailSerializer
    lookup_field = "id"
