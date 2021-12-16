from django.test import TestCase
from django.urls import reverse
from attendanceCode.models import AttendanceCode, AttendanceCodeForm, AttendanceLog, AttendanceLogForm
from keaclass.models import Class
from course.models import Course
from school.models import School
from teacher.models import Teacher
from subject.models import Subject
from django.test import Client

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

    def test_attendancecodeview_url_accessible_by_name(self):
        response = self.client.get(reverse('create attendance code'))
        self.assertEqual(response.status_code, 200)

    def test_attendancelogview_url_accessible_by_name(self):
        response = self.client.get(reverse('create attendance log'))
        self.assertEqual(response.status_code, 200)

    def test_attendancelistview_url_accessible_by_name(self):
        response = self.client.get(reverse('Attendance List'))
        self.assertEqual(response.status_code, 200)

    def test_attendancecode_create_post(self): # virker nok ikke
        url = reverse('create attendance code')
        c = Client()
        print("heeeeeeey")
        response = c.post(url, {
            'code': -91444444444474,
            'keaclass': self.Class,
            'subject': self.Subject,
            })
        self.assertEqual(response.status_code, 200)