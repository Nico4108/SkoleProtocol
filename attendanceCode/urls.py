from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from .views import AttendanceCodeFormView, AttendanceLogFormView, Attendancelogsuccess, Attendancecodesuccess, AttendanceList, loginsuccess

urlpatterns = [
    path('createattendancecode/', AttendanceCodeFormView.as_view(), name = "create attendance code"),
    path('createattendancelog/', AttendanceLogFormView.as_view(), name = "create attendance log"),
    path('success/', Attendancelogsuccess.as_view(), name = "success"),
    path('teachersucces/', Attendancecodesuccess.as_view(), name = "Teachersuccess"),
    path('showattendance/', AttendanceList.as_view(), name = "Attendance List"),
    path('loginsuccess/', views.loginsuccess),

]