from django.contrib import admin
from .models import Personal

#enables viewing and editing DB from admin page
admin.site.register(Personal)
