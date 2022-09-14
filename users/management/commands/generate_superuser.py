# create_multiple_users.py

import os

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from dotenv import load_dotenv
from users.models import User

load_dotenv()


class Command(BaseCommand):
    help = "Create superUser"

    def handle(self, *args, **kwargs):
        User.objects.create_superuser(
            username=os.getenv("ADMIN_USERNAME"),
            password=os.getenv("ADMIN_PASSWORD"),
            email=os.getenv("ADMIN_EMAIL"),
            birthdate="1999-9-9",
            first_name="admin",
            last_name="admin",
            is_staff=True
        )
