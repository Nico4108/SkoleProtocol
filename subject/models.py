from django.db import models
from teacher.models import Teacher
from student.models import Student

# Create your models here.
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    
    def __str__(self):
      return "{}".format(self.email)
    
    class Meta:
        db_table = 'Subject'


class StudentHasSubject(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
      return "{}".format(self.email)
    
    class Meta:
        db_table = 'StudentHasSubject'