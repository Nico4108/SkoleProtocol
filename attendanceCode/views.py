from django.shortcuts import render
from .models import AttendanceCode, AttendanceCodeForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.

# CreateView
class AttendanceCodeFormView(LoginRequiredMixin, CreateView):
    model = AttendanceCode
    template_name = "attendancecode/createattendancecode.html"
    form_class = AttendanceCodeForm
    success_url = "/attendancecode/createattendancecode/"

    # Checks if data input is valid and saves object
    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class AttendanceLogFormView(CreateView):
