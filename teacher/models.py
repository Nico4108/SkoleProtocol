from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
# Create your models here.

class Teacher(models.Model):    
    username = models.CharField(max_length=12, primary_key=True)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=40)
    Email = models.CharField(max_length=50)
    date_joined = models.DateField()
    REQUIRED_FIELDS = ['email', 'Username']
    
    def __str__(self):
      return "{}".format(self.username)
    
    class Meta:
        db_table = 'Teacher'