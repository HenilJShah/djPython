from django.urls import path
from . import views

urlpatterns = [
    path('fliterfile/',views.fliterfile, name="fliterfile"),
]