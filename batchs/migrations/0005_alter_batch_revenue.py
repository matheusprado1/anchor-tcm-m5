# Generated by Django 4.1.1 on 2022-09-14 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("batchs", "0004_batch_revenue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batch",
            name="revenue",
            field=models.FloatField(default=0),
        ),
    ]