from datetime import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Center, Manager, ControlCard, Group, Reporter, DocumentType, AuthorResolution, TypeSolution, \
    CheckFile, Letter, ControlFile
from django.contrib.auth.models import User


def login_function(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main:welcome')
    else:
        return redirect('main:login')


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
        if man.time_today:
            managers.append(man)
    content['managers'] = managers
    return content


def manager_control(request):
    content = content_need(request)
    manager = content['managers']
    managers = []
    for man in manager:
        if man.control:
            managers.append(man)
    content['managers'] = managers
    return content


def manager_out(request):
    content = content_need(request)
    manager = content['managers']
    managers = []
    for man in manager:
        if man.time_off:
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


def update_manager(request, manager_id):
    if request.method == 'POST':
        file = request.FILES['control_file']
        control_file = ControlFile.objects.create(file=file)
        control_file.save()
        summary = request.POST['summary']
        type_solution = TypeSolution.objects.get(name=request.POST['type_solution'])
        manager = Manager.objects.get(id=manager_id)
        letter = Letter.objects.get(id=manager.letter.id)

        letter.summary = summary
        letter.control = True
        letter.save()
        manager.control_file = control_file
        manager.letter.type_solution = type_solution
        if request.user.is_superuser:
            control = request.POST['control']
            if control == 'ok':
                manager.control = True
            elif control == 'no':
                manager.control = False
        manager.save()
        return redirect('main:welcome')


def admin_update_manager(request, manager_id):
    pass


def get_centers_post(request):
    center_name = request.POST.getlist('centers')
    print(center_name)
    centers = []
    for center in center_name:
        centers.append(Center.objects.get(name=center))
    print(centers)
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
        resolution=request.POST['resolution'],
        auth_resolution=selects['auth_resolution'],
        type_solution=selects['type_solution']
    )
    if letter:
        letter.save()
        return letter
    else:
        return redirect('main:manager-add')


def manager_create(request, content):
    manager = Manager.objects.create(
        letter=content['letter'],
        check_file=content['file'],
        lifetime=request.POST.get('lifetime')
    )
    for center in request.POST.getlist('centers'):
        manager.centers.add(Center.objects.get(name=center))
    manager.save()
    return manager


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


def get_user_function(request, user_id):
    content = content_need(request)
    user = User.objects.get(pk=user_id)
    center = [center for center in Center.objects.all() if center.user == user]
    content['user'] = user
    content['user_center'] = center
    content['users'] = User.objects.all()
    return content


def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('main:users')


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

