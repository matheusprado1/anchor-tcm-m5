import uuid

from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.db import models

MB = 1
MAX_SIZE = MB * 1024 * 1024


def validate_file_size(file):
    if file.size > MAX_SIZE:
        raise ValidationError("File exced maximum size 1MB")


class Image(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    photo = CloudinaryField(validators=[validate_file_size])

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="images",
        default="",
        null=True,
    )
    event = models.ForeignKey(
        "events.Event",
        on_delete=models.CASCADE,
        related_name="images",
        default="",
        null=True,
    )

    def photo_link(self):
        return f"https://res.cloudinary.com/anchorteam/image/upload/{self.photo}.jpg"
