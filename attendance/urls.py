from . import views
from django.urls import path

app_name, urlpatterns = "attendance", [
    path("invite/<id>/status/", views.invite_view, name="invite-view"),
    path("mark/<id>/attendance/", views.attendance_view, name="attendance-view"),
]
