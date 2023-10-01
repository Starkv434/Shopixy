# Generated by Django 4.2.4 on 2023-09-01 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("user_accounts", "0002_alter_profile_creation_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="city",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="profile",
            name="locality",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="profile",
            name="name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="profile",
            name="pincode",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="state",
            field=models.CharField(
                choices=[
                    ("Andhra Pradesh", "Andhra Pradesh"),
                    ("Arunachal Pradesh", "Arunachal Pradesh"),
                    ("Assam", "Assam"),
                    ("Bihar", "Bihar"),
                    ("Chhattisgarh", "Chhattisgarh"),
                    ("Goa", "Goa"),
                    ("Gujarat", "Gujarat"),
                    ("Haryana", "Haryana"),
                    ("Himachal Pradesh", "Himachal Pradesh"),
                    ("Jharkhand", "Jharkhand"),
                    ("Karnataka", "Karnataka"),
                    ("Kerala", "Kerala"),
                    ("Madhya Pradesh", "Madhya Pradesh"),
                    ("Maharashtra", "Maharashtra"),
                    ("Manipur", "Manipur"),
                    ("Meghalaya", "Meghalaya"),
                    ("Mizoram", "Mizoram"),
                    ("Nagaland", "Nagaland"),
                    ("Odisha", "Odisha"),
                    ("Punjab", "Punjab"),
                    ("Rajasthan", "Rajasthan"),
                    ("Sikkim", "Sikkim"),
                    ("Tamil Nadu", "Tamil Nadu"),
                    ("Telangana", "Telangana"),
                    ("Tripura", "Tripura"),
                    ("Uttarakhand", "Uttarakhand"),
                    ("Uttar Pradesh", "Uttar Pradesh"),
                    ("West Bengal", "West Bengal"),
                ],
                default=django.utils.timezone.now,
                max_length=100,
            ),
            preserve_default=False,
        ),
    ]
