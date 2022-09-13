import uuid

from batchs.models import Batch
from django.db import models
from tickets.models import Ticket


class Zone(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    total_sold_tickets = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    event = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE, related_name="zones"
    )

    def get_sold_tickets(self):
        qsBatchs = Batch.objects.filter(zone=self)
        tst = sum([len(batch.tickets.all()) for batch in qsBatchs])
        self.total_sold_tickets = tst
        self.save()
        return tst
