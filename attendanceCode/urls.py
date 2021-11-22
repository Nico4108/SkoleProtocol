from django.urls import path
# from django.views.generic.base import TemplateView
from .views import AttendanceCodeFormView

urlpatterns = [
    path('createattendancecode/', AttendanceCodeFormView.as_view(), name = "create attendance code"),
]