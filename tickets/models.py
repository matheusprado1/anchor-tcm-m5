from uuid import uuid4

from django.db import models


class Ticket(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tickets"
    )
    batch = models.ForeignKey(
        "batchs.Batch", on_delete=models.CASCADE, related_name="tickets"
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
