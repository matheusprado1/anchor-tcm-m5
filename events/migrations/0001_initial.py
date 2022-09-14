# Generated by Django 4.1.1 on 2022-09-14 16:38

from django.db import migrations, models
import django.db.models.deletion
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
                ("name", models.CharField(max_length=127)),
                ("description", models.TextField()),
                ("duration", models.IntegerField()),
                ("date", models.DateTimeField()),
                ("classification", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "address",
                    models.ForeignKey(
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="events",
                        to="addresses.address",
                    ),
                ),
            ],
        ),
    ]
