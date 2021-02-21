from django.db import models

# Create your models here.

class Promise(models.Model):
   #title = models.CharField(max_length=300)
   #description = models.TextField(blank=True)
   start_date= models.DateField()
   end_date = models.DateField()
#return null