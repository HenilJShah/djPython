from django.urls import path
from .views import home

urlpatterns = [
    path('form', home, name="home"),
]