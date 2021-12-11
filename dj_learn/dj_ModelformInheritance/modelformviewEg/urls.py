from django.urls import path
from .views import staffReg, stuReg
urlpatterns = [
    path('stu/',stuReg),
    path('stf/',staffReg),
]
