import uuid

from addresses.models import Address
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.utils import MyUserManager


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    cpf = models.CharField(max_length=14, unique=True, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField()
    birthdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.DO_NOTHING,
        related_name="users",
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "birthdate"]
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        return super(User, self).save(*args, **kwargs)


class Image(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    title = models.CharField(max_length=50)
    photo = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(
        "users.User",
        on_delete=models.DO_NOTHING,
        default="",
        null=True,
    )
