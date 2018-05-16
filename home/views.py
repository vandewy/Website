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

def projects(request):
    me = Personal.objects.all()

    context = {
        'me': me,
    }
    return render(request, 'home/projects.html', context)

def contact(request):
    me = Personal.objects.all()

    context = {
        'me': me,
    }
    return render(request, 'home/contact.html', context)
