from django.test import SimpleTestCase
from django.urls import reverse, resolve
from attendanceCode.views import AttendanceCodeFormView, AttendanceLogFormView, AttendanceList


class TestUrls(SimpleTestCase):
    def test_AttendanceCodeFormView_url_is_resolved(self):
        url = reverse('create attendance code')
        self.assertEquals(resolve(url).func.view_class, AttendanceCodeFormView)

    def test_AttendanceLogFormView_url_is_resolved(self):
        url = reverse('create attendance log')
        self.assertEquals(resolve(url).func.view_class, AttendanceLogFormView)

    def test_AttendanceList_url_is_resolved(self):
        url = reverse('Attendance List')
        self.assertEquals(resolve(url).func.view_class, AttendanceList)
