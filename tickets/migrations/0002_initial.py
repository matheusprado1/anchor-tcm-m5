# Generated by Django 4.1.1 on 2022-09-13 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
