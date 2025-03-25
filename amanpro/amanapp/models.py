from django.db import models

# Create your models here.



class New(models.Model):
    name=models.CharField(max_length=250)
    olm=models.CharField(max_length=250)
