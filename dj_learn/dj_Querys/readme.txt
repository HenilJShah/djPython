
title: query
~>new things in django i learn : 1


NOTE: write query in view.py 

youtube link: https://youtu.be/dihtmtYQgA4?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=96


referce link:

code part: 
------------------------------------------------------------------------------
python manage.py shell
-------------------------------
all() = return current data
"ModelClassName.objects.all()"
------------------------------------------------------------------------------

title: list_display
~>new things in django i learn : 2


NOTE: write admin.py file

youtube link: https://youtu.be/O_SsSeB-HSY?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=632


referce link:

code part: 
------------------------------------------------------------------------------
list_display()
-------------------------------
admin.py

from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display  = ('id', 'stuname','phno', 'des')
    

admin.site.register(Student, StudentAdmin)


models.py


from django.db import models

# Create your models here.
class Student(models.Model):
    stuname = models.CharField(max_length=15)
    phno = models.CharField(max_length=15)
    des = models.CharField(max_length=15)

------------------------------------------------------------------------------


title: register model by decorator
~>new things in django i learn : 3


NOTE: write admin.py file

youtube link: https://youtu.be/O_SsSeB-HSY?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=1099


referce link:

code part: 
------------------------------------------------------------------------------
@admin.register(ModelClassName1,ModelClassName2,ModelClassName3,..,site=custom_admin_site)
-------------------------------
admin.py

from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display  = ('id', 'stuname','phno', 'des')
    

admin.site.register(Student, StudentAdmin)


models.py


from django.db import models

# Create your models here.
class Student(models.Model):
    stuname = models.CharField(max_length=15)
    phno = models.CharField(max_length=15)
    des = models.CharField(max_length=15)

------------------------------------------------------------------------------
