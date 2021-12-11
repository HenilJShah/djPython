from django.urls import path
from . import views

urlpatterns = [
    path('app_1',views.app1_home1, name="app"),
    path('app_2',views.app1_home2, name="app"),
]