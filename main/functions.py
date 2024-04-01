from datetime import datetime

from .models import Center, Manager, ControlCard, Group, Reporter, DocumentType, AuthorResolution, TypeSolution


# def all_manager_count(request):
#     center = Center.objects.get(user__username=request.user.username)
#     manager = Manager.objects.all()
#     managers = []
#
#     if not center.user.is_superuser:
#         for man in manager:
#             if center in man.get_centers:
#                 managers.append(man)
#     else:
#         managers = manager
#


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
    content = {
        'centers': Center.objects.all(),  # Markazlar.
        'control_cards': ControlCard.objects.all(),  # Тип контрольной карточки Nazorat kartasining turi
        'groups': Group.objects.all(),  # Группа Guruh
        'reporters': Reporter.objects.all(),  # Корреспондент Muhbir
        'document_types': DocumentType.objects.all(),  # Тип документа Hujjat turi
        'author_resolutions': AuthorResolution.objects.all(),  # # Автор резолюции Qaror muallifi
        'type_solutions': TypeSolution.objects.all(),  # Вид решения Yechim turi
    }
    return content
