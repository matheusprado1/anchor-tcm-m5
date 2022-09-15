import uuid

from django.db import models


class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    description = models.TextField()
    duration = models.IntegerField()
    date = models.DateTimeField()
    classification = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="events",
        default="",
        null=True,
    )
    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="events",
        default="",
        null=True,
    )
