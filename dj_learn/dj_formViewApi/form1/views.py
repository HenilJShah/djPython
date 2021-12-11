from django.shortcuts import render

from .forms import l1Form

# Create your views here.
def home(request):
    fm = l1Form()
    print(fm)
    return render(request, 'index.html', {'fm':fm})