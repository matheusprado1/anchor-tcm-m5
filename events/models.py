import uuid

from django.db import models


class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    # photo = models.ImageField()
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=10)
    duration = models.IntegerField() # analisar posteriormente
    # distance = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    date = models.DateTimeField()
    full_age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    # user = models.ForeignKey(
    #     "users.User", on_delete=models.CASCADE, related_name="events"
    # )
    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="events",
        null=True,
        blank=True,
    )
