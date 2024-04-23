from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

DAYS = [(i, i) for i in ["monday", "tuesday", "wednesday", "thursday", "friday"]]


class Course(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True)
    students = models.ManyToManyField(User, related_name="students")
    lecturer = models.ForeignKey(User, models.CASCADE, related_name="courses")

    def __str__(self):
        return f"Course: {self.name} - {self.lecturer}"


class TimeTable(models.Model):
    end_time = models.TimeField()
    start_time = models.TimeField()
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["day"]

    def __str__(self):
        return f"{self.course} - {self.day} - {self.start_time} - {self.end_time}"
