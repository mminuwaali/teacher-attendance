from . import models
from django.contrib import admin


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["lecturer"]
    list_display = ["name", "lecturer", "created_at", "updated_at"]


@admin.register(models.TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_filter = ["day", "course"]
    list_display = ["course", "day", "start_time", "end_time"]
