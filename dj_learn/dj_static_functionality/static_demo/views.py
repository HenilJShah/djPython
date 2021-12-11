from django.shortcuts import render

# Create your views here.


def home(reuqest):
    context = {
        'nm': 'django',
        'num': 300,
    }
    return render(reuqest, 'index.html', context)
