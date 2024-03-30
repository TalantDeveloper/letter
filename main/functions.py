from .models import Center, Manager


def content_need(request):
    center = Center.objects.get(user__username=request.user.username)
    if center.user.is_superuser:
        managers = Manager.objects.all()
    else:
        managers = Manager.objects.filter(center=center)
    content = {
        'center': center,
        'managers': managers
    }
    return content
