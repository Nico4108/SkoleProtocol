from django.db import models
from keaclass.models import Class
from subject.models import Subject

# Create your models here.
class AttendanceCode(models.Model):
    id =  models.IntegerField()
    code = models.IntegerField()
    keaclass = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
      return "{}".format(self.email)
    
    class Meta:
        db_table = 'AttendanceCode'