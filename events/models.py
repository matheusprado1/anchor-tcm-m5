import uuid
from django.db import models
from django.core.exceptions import ValidationError


MB = 1
MAX_SIZE = MB * 1024 * 1024

def validate_file_size(file):
  if file.size > MAX_SIZE:
    raise ValidationError("File exced maximum size {MB}MB")


class Event(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  photo = models.ImageField(validators=[validate_file_size], null=True, blank=True)
  name = models.CharField(max_length=127)
  description = models.TextField()
  duration = models.IntegerField()
  date = models.DateTimeField()
  full_age = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)

  # user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="events", default="")
  address = models.OneToOneField("addresses.Address", on_delete=models.DO_NOTHING, related_name="event", default="", null=True)
