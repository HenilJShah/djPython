from django.contrib import admin
from django.db.models.base import Model

from .models import RegisterUser

# Register your models here.
@admin.register(RegisterUser)
class RegUser(admin.ModelAdmin):
    list_display = ['id', 'stu', 'staff', 'email']