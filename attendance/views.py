from . import models
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.timezone import datetime


def invite_view(request, id):
    if request.method == "POST":
        status = bool(request.POST.get("status"))

        try:
            invite = models.Request.objects.get(id=id)
            invite.status = status
            invite.save()

            if status:
                models.StudentAttendance.objects.create(
                    student=request.user,
                    attendance=invite.attendance,
                )
            else:
                requests = models.Request.objects.filter(
                    attendance=invite.attendance, created_at__date=datetime.today()
                )
                students = invite.attendance.timetable.course.students.exclude(
                    id__in=requests.values_list("student_id", flat=True)
                )

                if students.exists():
                    student = students.order_by("?").first()
                    print("exists", student)
                    models.Request.objects.create(
                        student=student,
                        attendance=invite.attendance,
                    )

            messages.success(request, f"Invite {'accepted' if status else 'rejected'}")
        except:
            messages.error(request, f"{'Accept' if status else 'Reject'} invite failed")
    return redirect(request.META.get("HTTP_REFERER", "landing:index-view"))


def attendance_view(request, id):
    if request.method == "POST":
        status = bool(request.POST.get("status"))

        try:
            invite = models.StudentAttendance.objects.get(id=id)
            invite.status = status
            invite.save()

            class_attendance = models.StudentAttendance.objects.filter(
                attendance=invite.attendance
            )

            if class_attendance.filter(status__isnull=True).count() == 0:
                positive_count = class_attendance.filter(status=True).count()
                negative_count = class_attendance.filter(status=False).count()

            teacher_attendance = True if positive_count >= negative_count else False

            invite.attendance.status = teacher_attendance
            invite.attendance.save()

            messages.success(request, "Attendance marked")
        except:
            messages.error(request, "Failed to mark attendance")
    return redirect(request.META.get("HTTP_REFERER", "landing:index-view"))
