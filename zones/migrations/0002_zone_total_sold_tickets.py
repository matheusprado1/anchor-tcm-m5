# Generated by Django 4.1.1 on 2022-09-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zones", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="zone",
            name="total_sold_tickets",
            field=models.IntegerField(default=0),
        ),
    ]
