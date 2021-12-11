from django.db import models
# Create your models here.


class stud_tb(models.Model):
    stud_id = models.IntegerField()
    stud_name = models.CharField(max_length=70)
    stud_email = models.EmailField(max_length=70)
    stud_passwd = models.CharField(max_length=150)
