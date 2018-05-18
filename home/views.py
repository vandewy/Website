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

def radar_sim(request):

    return render(request, 'home/radar_sim.html')

def tower_sim(request):

    return render(request, 'home/tower_sim.html')

def this_website(request):

    return render(request, 'home/this_website.html')

def testing(request):

    return render(request, 'home/testing.html')

def web_scraping(request):

    return render(request, 'home/web_scraping.html')
