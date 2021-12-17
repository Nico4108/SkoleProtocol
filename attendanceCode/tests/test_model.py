from django.test import TestCase
from attendanceCode.models import AttendanceCode, AttendanceCodeForm, AttendanceLog, AttendanceLogForm
from keaclass.models import Class
from course.models import Course
from school.models import School
from teacher.models import Teacher
from subject.models import Subject
from datetime import date

class Testmodels(TestCase):
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

        self.attendanceCode1 = AttendanceCode.objects.create(
            id = 1,
            code = -214748,
            keaclass = self.Class,
            subject = self.Subject,
        )

        self.attendanceCode3 = AttendanceCode.objects.create(
            code = 2147483,
            keaclass = self.Class,
            subject = self.Subject,
        )

        self.attendanceLog = AttendanceLog.objects.create(
            attendanceCode= 2147483, 
            keaclass= self.Class, 
            subject=self.Subject
        )

    def test_attendancecode_model(self):
        data = self.attendanceCode2 
        self.assertTrue(isinstance(data, AttendanceCode))
        self.assertEqual(str(data), ("50 SDi21 Testing "+str(date.today())+" True"))
    
    def test_attendancecode_model(self):
        data = self.attendanceCode3 
        self.assertTrue(isinstance(data, AttendanceCode))
        self.assertEqual(str(data), ("2147483 SDi21 Testing "+str(date.today())+" True"))

    def test_attendancelog_model(self):
        data = self.attendanceLog 
        self.assertTrue(isinstance(data, AttendanceLog))
        self.assertEqual(str(data), ("2147483  SDi21 Testing "+str(date.today())+" 55.70636 12.53917"))



 