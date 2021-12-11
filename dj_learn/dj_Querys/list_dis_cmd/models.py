from django.db import models

# Create your models here.
class Student(models.Model):
    stuname = models.CharField(max_length=15)
    phno = models.CharField(max_length=15)
    des = models.CharField(max_length=15)