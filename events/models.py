import uuid

# from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.db import models

MB = 1
MAX_SIZE = MB * 1024 * 1024


def validate_file_size(file):
    if file.size > MAX_SIZE:
        raise ValidationError("File exced maximum size {MB}MB")


class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    # photo = CloudinaryField(validators=[validate_file_size])
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
        on_delete=models.DO_NOTHING,
        related_name="events",
        default="",
        null=True,
    )
