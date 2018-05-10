from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL) #Bad case
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.user