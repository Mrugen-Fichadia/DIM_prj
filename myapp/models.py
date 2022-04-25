from django.db import models

class profile(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Contact_no = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=30)
    
    def __str__(self):
        return ((self.First_name)+"_"+(self.Last_name))