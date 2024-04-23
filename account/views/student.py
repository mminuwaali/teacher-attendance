from account import forms
from django.shortcuts import render
from timetable.models import TimeTable
from django.utils.timezone import datetime, now
from attendance.models import Request, Attendance, StudentAttendance
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name="student").exists())
def index_view(request):
    invites = Request.objects.filter(status__isnull=True, student=request.user)
    student_attendances = StudentAttendance.objects.filter(student=request.user)

    pendings = student_attendances.filter(status__isnull=True)
    histories = student_attendances.filter(status__isnull=False)
    timetable_today = TimeTable.objects.filter(day=now().strftime("%A").lower())

    print(timetable_today)

    context = {
        "invites": invites,
        "pendings": pendings,
        "histories": histories,
        "timetable_today": timetable_today,
    }
    return render(request, "student/index.html", context)
