from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def app2_home1(request):
    return HttpResponse("app2 hello app1")



def app2_home2(request):
    return HttpResponse("app2 hello app2")


