from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
from django.forms import ModelForm


# Create your models here.
class User(AbstractUser, models.Model):   
    kind_of_user =  models.CharField(max_length=12)
    username_fk = models.CharField(max_length=12)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'username_fk', 'kind_of_user']
    
    def __str__(self):
      return "{}".format(self.username_fk)
    
    class Meta:
        db_table = 'User'