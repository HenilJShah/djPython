from django.db import models

# Create your models here.
class StudentDbCrud(models.Model):
    name = models.CharField(max_length=255)
    email=models.EmailField()
    password = models.CharField(max_length=255)
