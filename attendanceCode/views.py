from django.shortcuts import render
from .models import AttendanceCode, AttendanceCodeForm, AttendanceLog, AttendanceLogForm
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from keaclass.models import Class
from student.models import Student
from subject.models import Subject, StudentHasSubject
from datetime import date
from course.models import Course
from school.models import School
import geopy.distance
from datetime import datetime
import pytz
from .calls import get_statstic, get_statstic_class
# from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.

# CreateView
class AttendanceCodeFormView(CreateView):
    model = AttendanceCode
    template_name = "attendancecode/Createattendancecode.html"
    form_class = AttendanceCodeForm
    success_url = "/attendancecode/teachersucces/"


    # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = "nadi6548"
        tz_EU = pytz.timezone('Europe/Copenhagen')
        now = datetime.now(tz_EU)
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        obj.time = current_time
        obj.save()
        return super().form_valid(form)

class AttendanceLogFormView(CreateView):
    model = AttendanceLog
    template_name = "attendancecode/Createattendancelog.html"
    form_class = AttendanceLogForm
    success_url = "/attendancecode/success/"

    # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit=False)
        user = "nadi6548"
        obj.date = date.today()
        getClass = Class.objects.get(name=obj.keaclass)
        getCourse = Course.objects.get(name=getClass.Course_name)
        getLocation = School.objects.get(id=getCourse.location_id)
        coords_1 = (getLocation.lat, getLocation.long)
        coords_2 = (obj.lat, obj.long)
        # check location and that student goes in the class HUSK AT ÆNDRE
        if (geopy.distance.distance(coords_1, coords_2).km < 0.5) and Student.objects.get(
                username=user, Class_id=obj.keaclass):
            # check log is a code with correct info and correct date and that
            # student has subject + code is active
            if AttendanceCode.objects.filter(
                    code=obj.attendanceCode,
                    keaclass_id=obj.keaclass,
                    subject_id=obj.subject_id,
                    date=obj.date,
                    isActive="True") and StudentHasSubject.objects.get(
                    student_name_id=user,
                    subject_name_id=obj.subject_id):
                obj.username_fk = user
                obj.save()
                return super().form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return render(self.request, './attendancecode/error.html')


class Attendancelogsuccess(TemplateView):
    template_name = "./attendancecode/studentregistersucces.html"


class Attendancecodesuccess(TemplateView):
    template_name = "./attendancecode/teacherregistersucces.html"


class AttendanceList(ListView):
    model = AttendanceLog
    template_name = "./attendancecode/showattendance.html"

    def get_queryset(self):
        class_val = self.request.GET.get('class')
        subject_val = self.request.GET.get('subject')
        user = self.request.user
        if class_val is not None and subject_val is not None:
            if subject_val == "None" or subject_val == "":
                return get_statstic_class(class_val)
            else:
                sub = Subject.objects.get(name=subject_val).id
                return get_statstic(class_val, sub)
        else:
            return AttendanceLog.objects.none()

    def get_context_data(self, **kwargs):
        context = super(AttendanceList, self).get_context_data(**kwargs)
        context['class'] = self.request.GET.get('class')
        context['subject'] = self.request.GET.get('subject')
        return context


def loginsuccess(request):
    return render(request, "attendancecode/Loginsuccess.html")


def get_stats(request, keaclass, subject):
    get_statstic("SDi21", 2)
    return render(request, "attendancecode/stat.html")

