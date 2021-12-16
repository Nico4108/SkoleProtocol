from django.test import TestCase
from attendanceCode.models import AttendanceCode, AttendanceCodeForm, AttendanceLog, AttendanceLogForm
from keaclass.models import Class
from course.models import Course
from school.models import School
from teacher.models import Teacher
from subject.models import Subject

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
            code = -2147483648,
            keaclass = self.Class,
            subject = self.Subject,
            date = "2021-02-02",
            time = "12:12:12",
            isActive = "True",
        )
        
        self.attendanceCode2 = AttendanceCode.objects.create(
            id = 2,
            code = 50,
            keaclass = self.Class,
            subject = self.Subject,
            date = "2021-02-02",
            time = "12:12:12",
            isActive = "True",
        )

        self.attendanceCode3 = AttendanceCode.objects.create(
            id = 3,
            code = 2147483649,
            keaclass = self.Class,
            subject = self.Subject,
            date = "2021-02-02",
            time = "12:12:12",
            isActive = "True",
        )

        self.attendanceLog = AttendanceCode.objects.create(
            id = 3,
            code = 2147483649,
            keaclass = self.Class,
            subject = self.Subject,
            date = "2021-02-02",
            time = "12:12:12",
            isActive = "True",
        )
    '''  
    def test_attendancecode_model(self):
        data = self.attendanceCode1
        self.assertTrue(isinstance(data.code.is_valid())) # ret så den ikke failer, men den siger good

    def test_attendancecode_model(self):
        data = self.attendanceCode2 
        self.assertTrue(isinstance(data, AttendanceCode))
    
    def test_attendancecode_model(self):
        data = self.attendanceCode3 
        self.assertFalse(isinstance(data, AttendanceCode)) # ret så den ikke failer, men den siger good
    ''' 