from django.shortcuts import render
from .models import AttendanceCode, AttendanceCodeForm, AttendanceLog, AttendanceLogForm
from django.views.generic import CreateView, TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.shortcuts import render
from subject.models import Subject, StudentHasSubject
from keaclass.models import Class
from student.models import Student
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from course.models import Course
from school.models import School
import geopy.distance
from datetime import datetime
import pytz
# from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.

# CreateView
class AttendanceCodeFormView(LoginRequiredMixin, CreateView):
    model = AttendanceCode
    template_name = "attendancecode/Createattendancecode.html"
    form_class = AttendanceCodeForm
    success_url = "/attendancecode/teachersucces/"


    # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.user = self.request.user
        tz_EU = pytz.timezone('Europe/Copenhagen') 
        now = datetime.now(tz_EU)
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        obj.time = current_time
        obj.save()
        return super().form_valid(form)


class AttendanceLogFormView(LoginRequiredMixin, CreateView):
    model = AttendanceLog
    template_name = "attendancecode/Createattendancelog.html"
    form_class = AttendanceLogForm
    success_url = "/attendancecode/success/"

      # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit = False)
        user = self.request.user
        obj.date = date.today()
        getClass = Class.objects.get(name=obj.keaclass)
        getCourse = Course.objects.get(name=getClass.Course_name)
        getLocation = School.objects.get(id=getCourse.location_id)
        coords_1 = (getLocation.lat, getLocation.long)
        coords_2 = (obj.lat, obj.long)
        #check location and that student goes in the class 
        if (geopy.distance.distance(coords_1, coords_2).km > 0.5) and Student.objects.get(username=user.username, Class_id=obj.keaclass):
            #check log is a code with correct info and correct date and that student has subject
            if AttendanceCode.objects.filter(code=obj.attendanceCode, keaclass_id=obj.keaclass, subject_id = obj.subject_id, date=obj.date, isActive="True") and StudentHasSubject.objects.get(student_name_id=user.username, subject_name_id=obj.subject_id):
                obj.username_fk = user.username
                obj.save()
                return super().form_valid(form)
            else:
                return render(self.request, './attendancecode/error.html')
        else:
            return render(self.request, './attendancecode/error.html')

class Attendancelogsuccess(LoginRequiredMixin, TemplateView):
    template_name = "./attendancecode/studentregistersucces.html"

class Attendancecodesuccess(LoginRequiredMixin, TemplateView):
    template_name = "./attendancecode/teacherregistersucces.html"


class AttendanceList(LoginRequiredMixin, ListView):
    model = AttendanceLog
    template_name = "./attendancecode/showattendance.html"


    def get_queryset(self):
       class_val = self.request.GET.get('class')
       subject_val = self.request.GET.get('subject')
       sub = Subject.objects.filter(name=subject_val).first()
       new_context = AttendanceLog.objects.filter(keaclass_id=class_val, subject_id=sub)
       return new_context

    def get_context_data(self, **kwargs):
        context = super(AttendanceList, self).get_context_data(**kwargs)
        context['class'] = self.request.GET.get('class')
        context['subject'] = self.request.GET.get('subject')
        return context

def loginsuccess(request):
    return render(request, "attendancecode/Loginsuccess.html")