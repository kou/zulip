# Generated by Django 1.11.16 on 2018-12-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0200_remove_preregistrationuser_invited_as_admin"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="zoom_api_key",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="realm",
            name="zoom_api_secret",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="realm",
            name="zoom_user_id",
            field=models.TextField(default=""),
        ),
    ]
