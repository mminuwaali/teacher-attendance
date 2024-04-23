from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Attendance(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    timetable = models.ForeignKey("timetable.timetable", models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.timetable} - {self.status}"


class StudentAttendance(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(User, models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    attendance = models.ForeignKey(Attendance, models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.student} - {self.attendance}"


class Request(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(User, models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    attendance = models.ForeignKey(Attendance, models.CASCADE)
    id = models.UUIDField(default=uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f"{self.student} - {self.attendance}"
