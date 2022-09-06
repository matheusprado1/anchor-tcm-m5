from rest_framework import generics

from batchs.models import Batch
from batchs.serializers import BatchDetailSerializer, BatchSerializer


class BatchsView(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class UpdateBatchsView(generics.UpdateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchDetailSerializer