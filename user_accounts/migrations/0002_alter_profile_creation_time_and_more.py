# Generated by Django 4.2.4 on 2023-08-31 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="creation_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="updated_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
