from datetime import time
from account import forms
from django.db.models import Avg
from django.shortcuts import render
from attendance.models import Attendance
from timetable.models import TimeTable, DAYS
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name="teacher").exists())
def index_view(request):
    timetable = []
    days = map(lambda x: x[0], DAYS)
    times = [[time(hour=i), time(hour=i + 1)] for i in range(8, 17)]

    table = TimeTable.objects.filter(course__lecturer=request.user)
    percentage = Attendance.objects.filter(
        status__isnull=False, timetable__course__lecturer=request.user
    ).aggregate(average=Avg("status"))

    for day in days:
        data = [day, []]
        for hour, _ in times:
            data[1].append(
                table.filter(
                    day=day,
                    end_time__gt=hour,
                    start_time__lte=hour,
                ).first()
                or ""
            )
        timetable.append(data)

    context = {
        "times": times,
        "timetable": timetable,
        "percentage": percentage["average"] * 100,
    }
    return render(request, "teacher/index.html", context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name="teacher").exists())
def history_view(request):
    attendances = Attendance.objects.filter(timetable__course__lecturer=request.user)

    context = {"attendances": attendances}
    return render(request, "teacher/history.html", context)
