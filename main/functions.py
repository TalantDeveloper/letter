from datetime import datetime
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from .models import Center, Manager, ControlCard, Group, Reporter, DocumentType, AuthorResolution, TypeSolution, \
    CheckFile, Letter
from django.contrib.auth.models import User


def content_need(request):
    center = Center.objects.get(user__username=request.user.username)
    manager = Manager.objects.all()
    managers = []

    if not center.user.is_superuser:
        for man in manager:
            if center in man.get_centers:
                managers.append(man)
    else:
        managers = manager
    jami = 0
    nazoratda = 0
    bajarilgan = 0
    muddati_utgan = 0
    muddat_bor = 0
    for man in managers:
        jami += 1
        if not man.control and man.control_file:
            nazoratda += 1
        if man.control:
            bajarilgan += 1
        if man.time_off and not man.control and not man.control_file:
            muddati_utgan += 1
        if not man.time_off:
            muddat_bor += 1
    content = {
        'center': center,
        'managers': managers,
        'jami': jami,
        'nazoratda': nazoratda,
        'bajarilgan': bajarilgan,
        'muddati_utgan': muddati_utgan,
        'muddat_bor': muddat_bor,
    }
    return content


def manager_today(request):
    content = content_need(request)
    manager = content['managers']
    managers = []
    for man in manager:
        if man.lifetime == datetime.now().date():
            managers.append(man)
    content['managers'] = managers
    return content


def manager_control_file(request):
    content = content_need(request)
    manager = content['managers']
    managers = []
    for man in manager:
        if man.control_file:
            managers.append(man)
    content['managers'] = managers
    return content


def manager_out(request):
    content = content_need(request)
    manager = content['managers']
    managers = []
    for man in manager:
        # print(man.time_on)
        if not man.control_file and man.lifetime < datetime.now().date():
            managers.append(man)
    content['managers'] = managers
    return content


def get_models_list(request):
    content = content_need(request)
    content = {
        'managers': content['managers'],
        'center': content['center'],
        'jami': content['jami'],
        'nazoratda': content['nazoratda'],
        'bajarilgan': content['bajarilgan'],
        'muddati_utgan': content['muddati_utgan'],
        'muddat_bor': content['muddat_bor'],
        'centers': Center.objects.all(),  # Markazlar.
        'control_cards': ControlCard.objects.all(),  # Тип контрольной карточки Nazorat kartasining turi
        'groups': Group.objects.all(),  # Группа Guruh
        'reporters': Reporter.objects.all(),  # Корреспондент Muhbir
        'document_types': DocumentType.objects.all(),  # Тип документа Hujjat turi
        'author_resolutions': AuthorResolution.objects.all(),  # # Автор резолюции Qaror muallifi
        'type_solutions': TypeSolution.objects.all(),  # Вид решения Yechim turi
    }
    return content


def create_check_file(request):
    file = request.FILES['check_file']
    check_file = CheckFile.objects.create(file=file)
    check_file.save()
    return check_file


def get_centers_post(request):
    center_name = request.POST.getlist('centers')
    centers = []
    for center in center_name:
        centers.append(Center.objects.get(name=center))
    return centers


def create_letter(request, selects):
    letter = Letter.objects.create(
        control_card=selects['control_card'],
        group=selects['group'],
        reporter=selects['reporter'],
        document_type=selects['document_type'],
        registration_date=request.POST['registration_date'],
        registration_number=request.POST['registration_number'],
        document_number=request.POST['document_number'],
        document_date=request.POST['document_date'],
        summary=request.POST['summary'],
        resolution=request.POST['resolution'],
        auth_resolution=selects['auth_resolution'],
        type_solution=selects['type_solution']
    )
    if letter:
        letter.save()
        return letter
    else:
        return redirect('main:manager-add')


def superuser_required(view_func):
    """
    Decorator for views that checks whether the user is a superuser,
    and returns HttpResponseForbidden if not.
    """

    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('main:welcome')
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def create_user(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = User.objects.create(
                username=username,
                password=password,
                first_name=full_name)
            if user:
                user.save()
                return redirect('main:users')
            else:
                return redirect('main:add-user')
        else:
            return redirect('main:add-user')


def get_center_edit(request, center_id):
    content = content_need(request)
    center = Center.objects.get(id=center_id)
    content['center_up'] = center
    content['centers'] = Center.objects.all()
    content['users'] = User.objects.all()
    return content


def center_edit(request, center_id):
    center = Center.objects.get(id=center_id)
    user = User.objects.get(id=request.POST['user_id'])
    center.name = request.POST['name']
    center.short = request.POST['short']
    center.user = user
    center.save()
    return redirect('main:centers')


def center_create(request):
    name = request.POST['center_name']
    short = request.POST['center_short']
    center = Center(name=name, short=short)
    if center:
        center.save()
        return redirect('main:centers')

