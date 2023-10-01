# Generated by Django 4.2.4 on 2023-09-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_accounts", "0008_alter_profile_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(
                default="static/default_pic.jpg", upload_to="profile_pic/"
            ),
        ),
    ]