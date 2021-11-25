from django.db import models
from keaclass.models import Class
from subject.models import Subject
from student.models import Student
from user.models import User
from django.forms import ModelForm

# Create your models here.
class AttendanceCode(models.Model):
    id =  models.AutoField(primary_key=True, )
    code = models.IntegerField(unique=True)
    keaclass = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
      return "{}".format(self.code)
    
    class Meta:
        db_table = 'AttendanceCode'


class AttendanceCodeForm(ModelForm):
    def init(self, args, **kwargs):
        super(AttendanceCodeForm, self).__init__(args, **kwargs)

    class Meta:
        model = AttendanceCode
        exclude = ('id', 'date')
        fields = '__all__'


class AttendanceLog(models.Model):
    attendanceCode = models.IntegerField()
    username_fk = models.CharField(max_length=12)
    keaclass = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.keaclass)
    
    class Meta:
        db_table = 'AttendanceLog'

class AttendanceLogForm(ModelForm):
    def init(self, args, **kwargs):
        super(AttendanceLogForm, self).__init__(args, **kwargs)

    class Meta:
        model = AttendanceLog
        exclude = ('username_fk', 'date')
        fields = '__all__'
