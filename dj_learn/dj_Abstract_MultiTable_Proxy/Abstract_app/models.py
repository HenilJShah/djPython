from tkinter.messagebox import NO
from django.db import models

# Create your models here.

# here the we create CommonInfo for common felids


class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True


class Students(CommonInfo):
    # name = models.CharField(max_length=70)
    # age = models.IntegerField()
    # date = models.DateField()
    # we don't want to inherit 'date' felids in this table
    # we can right like
    date = None
    feeds = models.IntegerField()


class Teachers(CommonInfo):
    # name = models.CharField(max_length=70)
    # age = models.IntegerField()
    salary = models.IntegerField()
    # we can overnight felids in abstract class : 'CommonInfo'
    date = models.DateField()


class Contractor(CommonInfo):
    # name = models.CharField(max_length=70)
    # age = models.IntegerField()
    payment = models.IntegerField()
