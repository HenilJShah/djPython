from django.contrib import admin
from .models import *
# Register your models here.



# here the we used decorators to register the dbclass
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ('id', 'stuname','phno', 'des')
    
# here the simple format
# admin.site.register(Student, StudentAdmin)
