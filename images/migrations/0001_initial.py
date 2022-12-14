# Generated by Django 4.1.1 on 2022-09-14 22:30

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import images.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                        max_length=255, validators=[images.models.validate_file_size]
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="events.event",
                    ),
                ),
            ],
        ),
    ]
