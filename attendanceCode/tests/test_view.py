from django.test import TestCase
from django.urls import reverse
from attendanceCode.models import AttendanceCode, AttendanceCodeForm, AttendanceLog, AttendanceLogForm
from keaclass.models import Class
from course.models import Course
from school.models import School
from teacher.models import Teacher
from subject.models import Subject
from django.test import Client
from datetime import date
from http import HTTPStatus

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

    def test_AttendanceCode_create_code_is_correct(self):
        attendancecode = AttendanceCode.objects.create(code= -9144444, keaclass= self.Class, subject=self.Subject)
        response = self.client.get(reverse('create attendance code'), kwargs={'code':attendancecode.code})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AttendanceCode.objects.last().code, -9144444)
    
    def test_Attendancelog_create_data_is_today(self):
        attendancelog = AttendanceLog.objects.create(attendanceCode= -9144444, keaclass= self.Class, subject=self.Subject)
        response = self.client.get(reverse('create attendance log'), kwargs={'attendanceCode':attendancelog.attendanceCode})
        self.assertEqual(response.status_code, 200)
        print(AttendanceLog.objects.last())
        self.assertEqual(AttendanceLog.objects.last().date, date.today())


    def test_post_new_attendance_log(self):
        response = self.client.post(reverse('create attendance log'), data={'code': "-1555555", 'keaclass':"SDi21", 'subject':'Testing'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_attendance_code_Form_code_is_required(self):
        response = self.client.post(reverse('create attendance code'), {'keaclass':"SDi21", 'subject':'Testing'})
        self.assertFormError(response, 'form', 'code', 'This field is required.')
    
    def test_attendance_code_Form_keaclass_is_required(self):
        response = self.client.post(reverse('create attendance code'), {'code': '-1555555', 'subject':'Testing'})
        self.assertFormError(response, 'form', 'keaclass', 'This field is required.')
    
    def test_attendance_code_Form_subject_is_required(self):
        response = self.client.post(reverse('create attendance code'), {'code': '-1555555', 'keaclass':"SDi21"})
        self.assertFormError(response, 'form', 'subject', 'This field is required.')