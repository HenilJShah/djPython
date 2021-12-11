from django.shortcuts import render

# Create your views here.
def ifelse(request):
    data = {
        'nm':'django',
        'st':5
    }
    return render(request, 'ifelse.html', data)