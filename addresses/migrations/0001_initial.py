# Generated by Django 4.1.1 on 2022-09-12 18:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("city", models.CharField(max_length=50)),
                ("district", models.CharField(max_length=100)),
                ("street", models.CharField(max_length=255)),
                ("number", models.CharField(max_length=30)),
                ("zipcode", models.CharField(max_length=20)),
            ],
        ),
    ]
