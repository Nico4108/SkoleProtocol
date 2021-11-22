from django.db import models
from school.models import School

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=45, default="")
    location = models.ForeignKey(School, on_delete=models.CASCADE, default="")


    def __str__(self):
      return "{}".format(self.name)
    
    class Meta:
        db_table = 'Course'
