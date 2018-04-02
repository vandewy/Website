from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ is default home
    url(r'^$', views.index, name='index'),
]