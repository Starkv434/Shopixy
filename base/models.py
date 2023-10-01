from django.db import models
import uuid


# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    creation_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True) 
    
    class Meta:
        abstract = True  # making this model as abstract class
        