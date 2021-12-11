from django.shortcuts import render
from .models import stud_tb
# Create your views here.


def home(request):
    stud = stud_tb.objects.all()
    context = {
        's':stud
    }
    return render(request, 'index.html', context)
