from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Manager, CheckFile, ControlFile, Letter, Center, ControlCard, Group, Reporter, DocumentType, \
    AuthorResolution, TypeSolution
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .functions import content_need, manager_today, manager_out, get_models_list, \
    create_check_file, create_letter, get_centers_post, superuser_required, create_user, center_edit, get_center_edit, \
    center_create, get_user_function, delete_user, login_function, manager_create, manager_control


def login_view(request):
    if request.method == 'POST':
        return login_function(request)
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return redirect('main:login')


@login_required
def welcome(request):
    content = content_need(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def today_view(request):
    content = manager_today(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def finish_view(request):
    content = manager_control(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def manager_out_view(request):
    content = manager_out(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def create_manager_view(request):
    content = get_models_list(request)
    if request.method == 'POST':

        control_card = ControlCard.objects.get(name=request.POST['control_card'])
        group = Group.objects.get(name=request.POST.get('group'))
        reporter = Reporter.objects.get(name=request.POST.get('reporter'))
        document_type = DocumentType.objects.get(name=request.POST.get('document_type'))
        auth_resolution = AuthorResolution.objects.get(name=request.POST.get('auth_resolution'))
        type_solution = TypeSolution.objects.get(name=request.POST.get('type_solution'))
        selects = {
            'control_card': control_card,
            'group': group,
            'reporter': reporter,
            'document_type': document_type,
            'auth_resolution': auth_resolution,
            'type_solution': type_solution
        }
        letter = create_letter(request, selects)
        centers = get_centers_post(request)
        file = create_check_file(request)
        mana = {
            'letter': letter,
            'centers': centers,
            'file': file
        }
        manager = manager_create(request, mana)
        return redirect('main:welcome')
    return render(request, 'main/home_create.html', context=content)


@login_required
def view_manager(request, manager_id):
    content = content_need(request)
    manager = Manager.objects.get(id=manager_id)
    content['manager'] = manager
    return render(request, 'main/home_update.html', context=content)


@login_required
@superuser_required
def view_centers(request):
    if request.method == 'POST':
        return center_create(request)
    content = content_need(request)
    centers = Center.objects.all()
    content['centers'] = centers
    return render(request, 'center/view_center.html', context=content)


@login_required
@superuser_required
def center_edit_view(request, center_id):
    if request.method == 'POST':
        return center_edit(request, center_id)
    content = get_center_edit(request, center_id)
    return render(request, 'center/center_update.html', context=content)


@login_required
@superuser_required
def delete_center(request, center_id):
    if request.method == 'POST':
        center = Center.objects.get(id=center_id)
        center.delete()
        return redirect('main:centers')
    content = content_need(request)
    return render(request, 'center/view_center.html', context=content)


@login_required
@superuser_required
def view_users(request):
    content = content_need(request)
    content['users'] = User.objects.all()
    return render(request, 'user/users.html', context=content)


@login_required
@superuser_required
def view_user(request, user_id):
    if request.method == 'POST':
        return delete_user(request, user_id)
    content = get_user_function(request, user_id)
    return render(request, 'user/user_view.html', context=content)


@login_required
@superuser_required
def create_user_view(request):
    content = content_need(request)
    content['centers'] = Center.objects.all()
    content['users'] = User.objects.all()
    if request.method == 'POST':
        return create_user(request)
    return render(request, 'user/add_user.html', context=content)

