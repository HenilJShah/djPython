from django.contrib import admin

from .models import StudentDbCrud

# Register your models here.


@admin.register(StudentDbCrud)
class StudentdbAdmin(admin.ModelAdmin):
    list_display = [f.name for f in StudentDbCrud._meta.get_fields()]