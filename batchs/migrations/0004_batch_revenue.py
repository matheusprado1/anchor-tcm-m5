# Generated by Django 4.1.1 on 2022-09-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("batchs", "0003_batch_total_sold_tickets"),
    ]

    operations = [
        migrations.AddField(
            model_name="batch",
            name="revenue",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
