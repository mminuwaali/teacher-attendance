from random import sample
from django.utils.timezone import datetime
from timetable.models import Course, TimeTable
from attendance.models import Request, Attendance
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create attendance requests for random students for all classes of the day"

    def handle(self, *args, **options):
        today = datetime.today()
        timetables = TimeTable.objects.filter(day=today.strftime("%A").lower())
        courses_today = Course.objects.filter(timetable__day=today)

        for timetable in timetables:
            if not Attendance.objects.filter(timetable=timetable, created_at__date=today.date()).exists():
                students = timetable.course.students.all()
                attendance = Attendance.objects.create(timetable=timetable)

                random_students = sample(list(students), min(3, len(students)))
                self.stdout.write(f"{students.count()} {random_students}")

                for student in random_students:
                    Request.objects.create(attendance=attendance, student=student)

        self.stdout.write("Request generated for all today's courses for 3 students")