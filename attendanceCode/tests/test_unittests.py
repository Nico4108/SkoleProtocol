from django.test import TestCase, SimpleTestCase
from attendanceCode.models import AttendanceCode, AttendanceLog
from keaclass.models import Class
from course.models import Course
from school.models import School
from subject.models import Subject
from teacher.models import Teacher
from student.models import Student
from django.urls import reverse
from django.test import Client
from attendanceCode.calls import get_statstic, get_statstic_class
from django.test import RequestFactory

# from django.contrib.auth import User 
from django.contrib.auth import get_user_model
User = get_user_model()
c = Client()
class TestForms(TestCase):
    def setUp(self):
       
        # Create user 
        test_user1 = User.objects.create_user(username='Andrea44', password='Mor12345')
        test_user1.save()

        test_school= School.objects.create(
            id=1,
            name="KEA",
            phone="20434565",
            adress="Guldbergsgade",
            lat=55.691510,
            long=12.555130
        )
        test_school.save()

        test_course1 = Course.objects.create(
            id=1,
            name="Software Development",
            department="Digital",
            location=test_school
        )
        test_course1.save()
        
        test_class1 = Class.objects.create(
            name="SDi21",
            year_started="2021",
            Course_name=test_course1
        )
        test_class1.save()
        test_teacher1 = Teacher.objects.create(
            username="Andera44",
            First_name="Andrea",
            Last_name="thomsen",
            Email="Andrea@test.dk",
            date_joined="2021-03-03"
        )
        test_teacher1.save()

        test_subject1= Subject.objects.create(
            name="Testing",
            teacher=test_teacher1
        )
        test_subject1.save()

        test_attendanceCode = AttendanceCode.objects.create(
             code=111,
            keaclass=test_class1,
            subject=test_subject1
        )
        test_attendanceLog = AttendanceLog.objects.create(
            attendanceCode=111,
            keaclass=test_class1,
            subject=test_subject1,
            lat=55.691510,
            long=12.555130
        )
        test_student = Student.objects.create()

class TestLogIn(TestCase):
    def test_user(self):
        c = Client()
        response = c.get('/accounts/login/', {'username': 'tester', 'password': 'testing1password1'})
        code = response.status_code
        self.assertEqual(code, 200)

    def test_view1(self):
        c = Client()
        url=reverse("create attendance code")
        response = c.post(url, {
            'code':'777',
            'keaclass':'SDi21',
            'subject':'1'
        })
        self.assertEqual(response.status_code, 200) 

    def test_get_queryset(self):
        keaclass = 'SDi21'
        response = get_statstic_class(keaclass)
        print(response)
    