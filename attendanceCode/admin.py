from django.contrib import admin
from .models import AttendanceCode, AttendanceLog

# Register your models here.
admin.site.register(AttendanceCode)
admin.site.register(AttendanceLog)
