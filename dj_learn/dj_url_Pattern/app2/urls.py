from django.urls import path
from . import views

urlpatterns = [
    path('app',views.app2_home1, name="app"),
]