from django.db import models

# Create your models here.
from django.db import models
from course.models import Course
from school.models import School


class Class(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    year_started = models.CharField(max_length=4)
    Course_name = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    
    def __str__(self):
      return "{}".format(self.email)
    
    class Meta:
        db_table = 'Class'

