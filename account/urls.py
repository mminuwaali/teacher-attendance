from . import views
from django.urls import path

app_name, urlpatterns = "account", [
    path("signup/", views.signup_view, name="signup-view"),
    path("signin/", views.signin_view, name="signin-view"),
    path("signout/", views.signout_view, name="signout-view"),
    # student dashboard
    path("student/", views.student.index_view, name="student-view"),
    # teacher dashboard
    path("teacher/", views.teacher.index_view, name="teacher-view"),
    path("teacher/history/", views.teacher.history_view, name="teacher-history-view"),
]
