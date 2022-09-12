from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from batchs.models import Batch
from batchs.serializers import BatchDetailSerializer, BatchSerializer
from batchs.permissions import OwnerOrSuperUserAuth, SuperUserAuth

class BatchsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OwnerOrSuperUserAuth]
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    lookup_field = "batch_id"


class UpdateBatchsView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OwnerOrSuperUserAuth]
    queryset = Batch.objects.all()
    serializer_class = BatchDetailSerializer
    lookup_field = "batch_id"
