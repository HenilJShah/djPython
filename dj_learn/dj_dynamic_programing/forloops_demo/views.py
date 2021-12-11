from django.shortcuts import render

# Create your views here.
def loops(request):
    return render(request, 'loops.html')