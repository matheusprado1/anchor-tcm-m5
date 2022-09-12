import uuid

from django.core.serializers import serialize
from django.db import models
from django.utils import timezone


class Batch(models.Model):

    id = models.UUIDField(  # mudei nome para id conforme outras tabela.
        default=uuid.uuid4, primary_key=True
    )
    price = models.FloatField()
    quantity = models.IntegerField()
    due_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    number_batch = models.SmallIntegerField()

    zone = models.ForeignKey(
        "zones.Zone", on_delete=models.CASCADE, related_name="batchs"
    )
