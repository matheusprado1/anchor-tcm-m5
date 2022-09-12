# Generated by Django 4.1.1 on 2022-09-12 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("batchs", "0001_initial"),
        ("zones", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="batch",
            name="zone",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="batchs",
                to="zones.zone",
            ),
        ),
    ]
