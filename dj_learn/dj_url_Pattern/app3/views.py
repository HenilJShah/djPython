from django.http.response import HttpResponse
from django.shortcuts import render



# Create your views here.
def app3_home1(request):
    return HttpResponse("app3 hello app1")



def app3_home2(request):
    return HttpResponse("app3 hello app2")
