import uuid

from django.db import models


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20, null=True)
    longitude = models.CharField(max_length=20, null=True)

    def get_full_address(self):
        return f"{self.street}, {self.number}. {self.city}, {self.zipcode}"
