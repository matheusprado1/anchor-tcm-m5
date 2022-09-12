from rest_framework import generics
from batchs.mixins import SerializerByMixin

from batchs.models import Batch
from batchs.serializers import BatchDetailSerializer, BatchSerializer


class BatchsView(SerializerByMixin, generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_map = {"GET": BatchSerializer,
                      "POST": BatchSerializer}



class UpdateBatchsView(SerializerByMixin, generics.UpdateAPIView):
    queryset = Batch.objects.all()
    serializer_map = {"PATCH": BatchDetailSerializer}

