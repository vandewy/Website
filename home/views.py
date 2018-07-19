from django.shortcuts import render
from .models import Personal
from django.http import Http404
import cgi
import smtplib
import sqlite3
import datetime


def send_email(user_name=None, user_email=None, user_message=None):
    print(user_name)

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

def message_sent(request):

    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('user_email')
        message = request.GET.get('message')
        date = datetime.datetime.today()


        db = sqlite3.connect('db.sqlite3')
        cur = db.cursor()
        cur.execute('''INSERT INTO messages (name, email, message, date_sent)
                          VALUES(?,?,?,?)''', (name, email, message, date,))
        db.commit()
        cur.close()
        db.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("vandewynkel@gmail.com", "doeb pgqt fdnw pokc")

        complete_message = '\n'
        complete_message += 'Name: ' + name + '\n'
        complete_message += 'Email: ' + email + '\n'
        complete_message += 'Message: ' + message + '\n'

        server.sendmail("vandewynkel@gmail.com", "vandewynkel@gmail.com", complete_message)
        server.quit()

    return render(request, 'home/message_sent.html')

