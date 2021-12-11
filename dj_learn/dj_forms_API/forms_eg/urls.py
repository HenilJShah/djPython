from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('welcome', views.newpage, name="newpage"),
    path('forms', views.formField_data, name="forms"),
]
