import uuid

from django.db import models


class Zone(models.Model):
  id                   = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  name                 = models.CharField(max_length=50)
  total_selled_tickets = models.IntegerField()
  is_active            = models.BooleanField(default=False)
  created_at           = models.DateTimeField(auto_now_add=True)

  event = models.ForeignKey("events.Event", on_delete=models.CASCADE, related_name="zones", default=
  "", null=True)