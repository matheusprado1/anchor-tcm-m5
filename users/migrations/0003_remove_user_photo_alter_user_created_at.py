# Generated by Django 4.1.1 on 2022-09-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_photo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="photo",
        ),
        migrations.AlterField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
