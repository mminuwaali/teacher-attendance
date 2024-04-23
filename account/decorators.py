from django.shortcuts import redirect


def role_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return redirect("admin:index")

            elif request.user.groups.filter(name="teacher").exists():
                return redirect("account:teacher-view")

            elif request.user.groups.filter(name="student").exists():
                return redirect("account:student-view")

        return function(request, *args, **kwargs)

    return wrap
