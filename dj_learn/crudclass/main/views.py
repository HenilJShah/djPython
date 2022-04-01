from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, RedirectView
from .models import StudentDb

from .forms import StudentForm
# Create your views here.


class UserAddShow(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentForm()
        stud = StudentDb.objects.all()
        context["stud"] = stud
        context["form"] = fm
        return context

    def post(self, request, **kwargs):
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
        else:
            print(fm.errors)
        return HttpResponseRedirect("/")


class UserUpdate(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        studdata = StudentDb.objects.get(id = kwargs["id"])
        fm = StudentForm(instance=studdata)
        context = super().get_context_data(**kwargs)
        context["form"] = fm
        context["stud"] = StudentDb.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        data = StudentDb.objects.get(id = kwargs["id"])
        fm = StudentForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save() if fm.is_valid() else print(fm.errors)
        return HttpResponseRedirect("/")

class UserDelete(RedirectView):
    url = reverse_lazy("user_adding")

    def get_redirect_url(self, *args, **kwargs):
        StudentDb.objects.get(id=kwargs["id"]).delete()
        return super().get_redirect_url(*args, **kwargs)
