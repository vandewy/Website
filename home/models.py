from django.db import models

# Create your models here.


class Personal(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contact_number = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    github_account = models.CharField(max_length=100)
    linkedin_account = models.CharField(max_length=100)


