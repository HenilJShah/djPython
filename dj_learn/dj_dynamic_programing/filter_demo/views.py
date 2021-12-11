from django.shortcuts import render
from datetime import datetime
# Create your views here.


def fliterfile(request):
    data = {
        "name": "heniL",
        "bootval": False,
        "strlen": "abcd",
        "tx": "hello world",

        "dt":datetime.now(),

        "val1":56.96220,
        "val2":56.000,
        "val3":56.37000,

    }
    return render(request, "fliter.html", data)
