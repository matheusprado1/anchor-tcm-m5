from django.db import models
from django.utils import timezone

import uuid


class Batch(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    price = models.IntegerField()
    quantity = models.IntegerField()
    number_batch = models.IntegerField()
    due_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    # zone = models.ForeignKey(
    #     "zones.Zone", on_delete=models.CASCADE, related_name="batchs"
    # )
