from django.shortcuts import render

# Create your views here.


def home(request):
    data = {
        'dj': 'django'
    }
    return render(request, "index.html", data)


def about(request):
    data = {
        'ab': 'about the django'
    }
    return render(request, "about.html", data)
