from django.db import models

# Create your models here.

class todo(models.Model):
    name = models.CharField(max_length=150)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)