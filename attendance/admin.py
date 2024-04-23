from . import models
from django.contrib import admin


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_filter = ["timetable", "status"]
    list_display = ["timetable", "status"]


@admin.register(models.StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_filter = ["student", "attendance", "status"]
    list_display = ["student", "attendance", "status"]


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    list_filter = ["student", "attendance", "status"]
    list_display = ["student", "attendance", "status"]
