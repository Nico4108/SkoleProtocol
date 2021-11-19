from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
from course.models import Course
from keaclass.models import Class

# Create your models here.

class Student(models.Model):    
    username = models.CharField(max_length=12, primary_key=True)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=40)
    Email = models.CharField(max_length=50)
    date_joined = models.DateField()
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    REQUIRED_FIELDS = ['email', 'Username']
    
    def __str__(self):
      return "{}".format(self.email)
    
    class Meta:
        db_table = 'Student'


