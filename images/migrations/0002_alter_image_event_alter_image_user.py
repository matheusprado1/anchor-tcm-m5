# Generated by Django 4.1.1 on 2022-09-12 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0002_initial"),
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="event",
            field=models.ForeignKey(
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="events.event",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="user",
            field=models.ForeignKey(
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
