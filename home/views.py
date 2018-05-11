from django.shortcuts import render
from .models import Personal
from django.http import Http404

def index(request):
    me = Personal.objects.all()

    #django automatically starts at templates
    #standard convention nameing 'context'/ is a dictionary
    context = {
        'me': me,
    }
    #httpresponse is built into render
    return render(request, 'home/index.html', context)
