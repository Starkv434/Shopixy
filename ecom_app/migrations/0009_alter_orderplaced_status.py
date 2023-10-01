# Generated by Django 4.2.4 on 2023-09-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecom_app", "0008_alter_orderplaced_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderplaced",
            name="status",
            field=models.CharField(
                choices=[
                    ("Accepted", "Accepted"),
                    ("Packed", "Packed"),
                    ("On the Way", "On the Way"),
                    ("Delivered", "Delivered"),
                    ("Cancel", "Cancel"),
                ],
                default="Accepted",
                max_length=50,
            ),
        ),
    ]
