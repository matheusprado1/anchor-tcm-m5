# Generated by Django 4.1.1 on 2022-09-13 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zones", "0003_rename_total_tickets_sold_zone_total_sold_tickets"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zone",
            name="total_sold_tickets",
            field=models.IntegerField(default=0),
        ),
    ]