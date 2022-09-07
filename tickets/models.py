from uuid import uuid4

from django.db import models


class ticket(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    user_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tickets"
    )
    batch_id = models.ForeignKey(
        "batchs.Batch", on_delete=models.CASCADE, related_name="tickets"
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
