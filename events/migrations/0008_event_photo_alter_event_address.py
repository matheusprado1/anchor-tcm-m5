# Generated by Django 4.1.1 on 2022-09-11 00:19

import cloudinary.models
import django.db.models.deletion
import events.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addresses", "0001_initial"),
        ("events", "0007_remove_event_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="photo",
            field=cloudinary.models.CloudinaryField(
                default=1,
                max_length=255,
                validators=[events.models.validate_file_size],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="event",
            name="address",
            field=models.ForeignKey(
                default="",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="event",
                to="addresses.address",
            ),
        ),
    ]
