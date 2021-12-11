from django.shortcuts import render

# Create your views here.
def userCreate(request):
    return render(request, "user.html")