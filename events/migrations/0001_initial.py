# Generated by Django 4.1.1 on 2022-09-10 21:51

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import events.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("addresses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "photo",
                    cloudinary.models.CloudinaryField(
                        max_length=255, validators=[events.models.validate_file_size]
                    ),
                ),
                ("name", models.CharField(max_length=127)),
                ("description", models.TextField()),
                ("duration", models.IntegerField()),
                ("date", models.DateTimeField()),
                ("full_age", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "address",
                    models.OneToOneField(
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="event",
                        to="addresses.address",
                    ),
                ),
            ],
        ),
    ]
