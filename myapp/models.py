from django.db import models
from django.db.models import Model
# Create your models here.

class profile(Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name