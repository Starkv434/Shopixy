from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.utils import timezone
# Create your models here.

STATE_CHOICES = [
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal')
]



class Profile(BaseModel):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    landmark = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    pincode = models.TextField(null=True, blank = True)
    state = models.CharField(choices = STATE_CHOICES, max_length=100)
    profile_pic = models.ImageField(upload_to="profile_pic/", default="static/default_pic.jpg")
    
    def __str__(self):
        return self.name

    

