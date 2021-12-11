from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    # normal form
    # fm = StudentRegistrationForm()

    # string with id
    # fm = StudentRegistrationForm(auto_id="some_%s")

    # fields with id
    # fm = StudentRegistrationForm(auto_id=True)

    # remove id
    # fm = StudentRegistrationForm(auto_id=False)

    # lable suffix = ":"
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = "=")
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = "A")
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = " ")

    # dynamic initial values
    # fm = StudentRegistrationForm(auto_id=True, label_suffix = " ", initial = {'name':"abc"})

    # field_order
    fm = StudentRegistrationForm(field_order=['name', 'email', 'phno'])

    fm_with_args = Student_with_args(initial={
        'name': 'Student'
    })

    fm_with_widget = Student_with_widget()

    if request.POST:
        fmvalid = StudentRegistrationForm_demo(request.POST)
        print(fmvalid)
        if fmvalid.is_valid():
            print(f"\n\n\n\ncleaned_data:{fmvalid.cleaned_data}\n\n\n\n")
            print(f"\n\n\n\nname:{fmvalid.cleaned_data['name']}\n\n\n\n")
            print(f"\n\n\n\nphno:{fmvalid.cleaned_data['phno']}\n\n\n\n")
            print(f"\n\n\n\nemail:{fmvalid.cleaned_data['email']}\n\n\n\n")
            print(f"\n\n\n\npasswd:{fmvalid.cleaned_data['passwd']}\n\n\n\n")
        # clear form fields
        # fmvalid = StudentRegistrationForm_demo()

        return HttpResponseRedirect('welcome')

    else:
        fmvalid = StudentRegistrationForm_demo()

    data = {
        "fm": fm,
        "eg_args": fm_with_args,
        "eg_widget": fm_with_widget,
        "eg_valid": fmvalid
    }
    return render(request, 'studentform.html', data)


def newpage(request):
    return render(request, 'welcome.html')


# Form Field Type
def formField_data(request):
    if request.POST:    
        fm = fieldForm(request.POST)
        if fm.is_valid():
            print(f"\n min_len:{fm.cleaned_data['min_len']}")
            print(f"\n max_len:{fm.cleaned_data['max_len']}")
            print(f"\n space_data:{fm.cleaned_data['space_data']}")
            print(f"\n empty_val:{fm.cleaned_data['empty_val']}")
            print(f"\n num:{fm.cleaned_data['num']}")
            fm = fieldForm()
        else:
            # fm = fieldForm()
            print(fm.errors)
    else:
        fm = fieldForm()
        print("\n\n",fm.errors)

    data = {
        "name":fm
    }
    return render(request, 'formsshow.html', data)
