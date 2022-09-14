import datetime as dt
import uuid

from django.core.serializers import serialize
from django.db import models
from django.utils import timezone
from tickets.models import Ticket


class Batch(models.Model):

    id = models.UUIDField(  
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

    def zone_name(self):
        return self.batch.zone.name

    def is_date_valid(self):
        today = dt.date.today()
        duedate = self.due_date
        if duedate > today:
            return True
        self.is_active = False
        self.save()
        return False

    def is_enough_tickets(self, num_tickets: int = 1):
        qs = Ticket.objects.filter(batch=self)
        if len(qs) + num_tickets < self.quantity:
            self.is_active = True
            self.save()
            return True
        if len(qs) + num_tickets == self.quantity:
            self.is_active = False
            self.save()
            return True
        return False
