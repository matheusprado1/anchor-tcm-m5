import datetime as dt
import uuid

from django.core.serializers import serialize
from django.db import models
from django.utils import timezone
from tickets.models import Ticket


class Batch(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    total_sold_tickets = models.IntegerField(default=0)
    due_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    number_batch = models.SmallIntegerField()

    zone = models.ForeignKey(
        "zones.Zone", on_delete=models.CASCADE, related_name="batchs"
    )

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

    def get_sold_tickets(self):
        tst = len(self.tickets.all())
        self.total_sold_tickets = tst
        self.save()
        return tst
