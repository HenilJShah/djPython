from django.shortcuts import render
from .forms import StaffUser, StuUser
# Create your views here.


def stuReg(request):
    fm = StuUser()
    if request.method == 'POST':
        fm = StuUser(request.POST)
        if fm.is_valid():
            fm.save()
        else:
            fm = StuUser()
    return render(request, 'stu.html', {"form":fm})

def staffReg(request):
    fm = StaffUser()
    if request.method == 'POST':
        fm = StaffUser(request.POST)
        if fm.is_valid():
            fm.save()
        else:
            fm = StaffUser()
    return render(request, 'staff.html', {"form":fm})
