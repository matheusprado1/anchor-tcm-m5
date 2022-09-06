# Generated by Django 4.1.1 on 2022-09-06 14:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("zones", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zone",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]