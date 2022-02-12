from django.contrib import admin

from .models import Contractor, Students, Teachers

# Register your models here.


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'feeds')


@admin.register(Teachers)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'salary', 'date')


@admin.register(Contractor)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'payment', 'date')
