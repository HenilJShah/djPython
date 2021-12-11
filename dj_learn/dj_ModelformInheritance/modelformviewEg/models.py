from django.db import models

# Create your models here.
class RegisterUser(models.Model):
    stu = models.CharField(max_length=50)
    staff = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)