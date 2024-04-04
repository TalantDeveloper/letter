from django.shortcuts import render, redirect
from .models import Manager, CheckFile, ControlFile, Letter, Center, ControlCard, Group, Reporter, DocumentType, \
    AuthorResolution, TypeSolution
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .functions import content_need, manager_today, manager_control_file, manager_out, get_models_list, \
    create_check_file, create_letter, get_centers_post, superuser_required


def login_view(request):
    if request.method == 'POST':
        print("Post")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            print("Kirdi")
            login(request, user)
            return redirect("main:welcome")
        else:
            return redirect('main:login')
    return render(request, 'user/login.html')


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
    content = manager_control_file(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def manager_out_view(request):
    content = manager_out(request)
    return render(request, 'main/welcome.html', context=content)


@login_required
def create_manager_view(request):
    content = get_models_list(request)
    if request.method == 'POST':
        file = create_check_file(request)
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
        manager = Manager.objects.create(
            letter=letter,
            check_file=file,
            lifetime=request.POST.get('lifetime')
        )
        manager.centers.add(*centers)
        manager.save()
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
def employee_add(request):
    content = content_need(request)
    content['centers'] = Center.objects.all()
    if request.method == 'POST':
        print(request.POST)
    if request.method == 'GET':
        print(request.GET)
    return render(request, 'user/add_user.html', context=content)


