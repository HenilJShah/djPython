from django.http.response import HttpResponse
from django.shortcuts import render



# Create your views here.
def app1_home1(request):
    return HttpResponse("app1 hello app1")



def app1_home2(request):
    return HttpResponse("app1 hello app2")
