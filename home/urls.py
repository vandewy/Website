from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ is default home
    url(r'^$', views.index, name='index'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^radar_sim/$', views.radar_sim, name='radar_sim'),
    url(r'^tower_sim/$', views.tower_sim, name='tower_sim'),
    url(r'^this_website/$', views.this_website, name='this_website'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^web_scraping/$', views.web_scraping, name='web_scraping'),

]