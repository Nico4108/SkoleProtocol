from django.test import TestCase, SimpleTestCase
from attendanceCode.models import AttendanceCode, AttendanceLog
from keaclass.models import Class as keaclasss
from course.models import Course
from school.models import School
from subject.models import Subject
from teacher.models import Teacher
from student.models import Student
from django.urls import reverse
from django.test import Client
import attendanceCode.calls as func
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
        
        test_class = keaclasss.objects.create(
            name="SDi21",
            year_started="2021",
            Course_name=test_course1
        )
        test_class.save()
        test_teacher1 = Teacher.objects.create(
            username="Andera44",
            First_name="Andrea",
            Last_name="thomsen",
            Email="Andrea@test.dk",
            date_joined="2021-03-03"
        )
        test_teacher1.save()

        test_subject1 = Subject.objects.create(
            name="Testing",
            teacher=test_teacher1
        )
        test_subject1.save()

        test_attendanceCode = AttendanceCode.objects.create(
             code=111,
            keaclass=test_class,
            subject=test_subject1
        )
        test_attendanceLog = AttendanceLog.objects.create(
            attendanceCode=111,
            keaclass=test_class,
            subject=test_subject1,
            lat=55.691510,
            long=12.555130
        )
        test_student = Student.objects.create(
            username = "Nadi6548",
            First_name = "nadia",
            Last_name = "hansen",
            Email = "test",
            date_joined = "2021-01-20" ,
            Course = test_course1,
            Class = test_class,
        )

    def test_user_log_in(self):
        c = Client()
        response = c.post('/accounts/login/', {'username': 'tester', 'password': 'testing1password1'})
        code = response.status_code
        self.assertEqual(code, 200)

    def test_post_method(self):
        c = Client()
        url=reverse("create attendance code")
        response = c.post(url, {
            'code':'777',
            'keaclass':'SDi21',
            'subject':'1'
        })
        self.assertEqual(response.status_code, 200) 

    def test_test(self):
        school1= {
            "id":"1",
            "name":"KEA",
            "phone":"20434565",
            "adress":"Guldbergsgade",
            "lat":"55.691510",
            "long":"12.555130"
        }
        course1 = {
            "id":"1",
            "name":"Software Development",
            "department":"Digital",
            "location":school1
        }
        keaclass1 = {
            "name":"SDi21",
            "year_started":"2021",
            "Course_name":course1
        }
    
    def test_test(self):
        view_url = reverse("create attendance code")
        expected_in_output = 'A1b2c9'
        data = {
            'code':'777',
            'keaclass':'SDi21',
            'subject':'1'
        }
            # stuff that will satisfy form.is_valid(), but fail the tests
            # in your form_valid method
        response=c.post( view_url, data)   
        self.assertIn(expected_in_output, response.content.decode() )
