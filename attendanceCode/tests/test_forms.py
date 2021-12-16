from django.test import TestCase
from attendanceCode.models import AttendanceCode, AttendanceCodeForm, AttendanceLog, AttendanceLogForm
from keaclass.models import Class
from course.models import Course
from school.models import School
from teacher.models import Teacher
from subject.models import Subject

class TestForms(TestCase):
    def setUp(self):
        self.School= School.objects.create(
            id=1,
            name="KEA",
            phone="20434565",
            adress="Guldbergsgade",
            lat=55.691510,
            long=12.555130
        )

        self.Course = Course.objects.create(
            id=1,
            name="Software Development",
            department="Digital",
            location=self.School
        )

        self.Class = Class.objects.create(
            name="SDi21",
            year_started="2021",
            Course_name=self.Course
            )
        
        self.Teacher = Teacher.objects.create(
            username="Andera44",
            First_name="Andrea",
            Last_name="thomsen",
            Email="Andrea@test.dk",
            date_joined="2021-03-03"
        )

        self.Subject= Subject.objects.create(
            name="Testing",
            teacher=self.Teacher
        )
  #ATTENDANCE CODE
    def test_AttendanceCode_form_valid_data(self):
            form = AttendanceCodeForm(data={
                'code': 21474,
                'keaclass': self.Class,
                'subject': self.Subject,
                })
            self.assertTrue(form.is_valid())
    
    def test_AttendanceCode_form_invalid_data(self):
            form = AttendanceCodeForm(data={
                'keaclass': self.Class,
                'subject': self.Subject,
                })
            self.assertFalse(form.is_valid())
    
    def test_AttendanceCode_form_no_data(self):
        form = AttendanceCodeForm(data={})
        self.assertFalse(form.is_valid())
    
    #ATTENDANCE LOG
    def test_AttendanceLog_form_valid_data(self):
        form = AttendanceLogForm(data={
            'attendanceCode': 21474,
            'keaclass': self.Class,
            'subject': self.Subject,
            'lat': 55.691510,
            'long': 12.555130
            })
        self.assertTrue(form.is_valid())
    
    def test_AttendanceLog_form_invalid_data(self):
        form = AttendanceLogForm(data={
            'keaclass': self.Class,
            'subject': self.Subject,
            'lat': 55.691510,
            'long': 12.555130
            })
        self.assertFalse(form.is_valid())
    
    def test_AttendanceLog_form_no_data(self):
        form = AttendanceLogForm(data={})
        self.assertFalse(form.is_valid())

    