# Create your models here.
from django.db import models
class waitlist(models.Model):
   name = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   phonenumber = models.CharField(max_length=200)
   position = models.CharField(max_length=200) 
   def __str__(self):
      return self.name