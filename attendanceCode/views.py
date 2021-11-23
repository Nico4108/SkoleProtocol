from django.shortcuts import render
from .models import AttendanceCode, AttendanceCodeForm, AttendanceLog, AttendanceLogForm
from django.views.generic import CreateView, TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.shortcuts import render
from subject.models import Subject
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
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
        obj.username_fk = user.username
        if AttendanceCode.objects.filter(code=obj.attendanceCode, keaclass_id=obj.keaclass, subject_id = obj.subject, date=obj.date):
            obj.save()
            return super().form_valid(form)
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