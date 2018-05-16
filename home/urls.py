from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ is default home
    url(r'^$', views.index, name='index'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^contact/$', views.contact, name='contact'),
]