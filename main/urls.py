from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('today/', views.today_view, name='today'),
    path('finish/', views.finish_view, name='finish'),
    path('timeout/', views.manager_out_view, name='timeout'),

    path('manager-add/', views.create_manager_view, name='manager-add'),
    path('manager-view/<int:manager_id>/', views.view_manager, name='manager-view'),

    path('centers/', views.view_centers, name='centers'),
    path('centers/<int:center_id>/update/', views.center_edit_view, name='center-edit'),
    path('centers/<int:center_id>/delete/', views.delete_center, name='center-delete'),

    path('users/', views.view_users, name='users'),
    path('users/<int:user_id>', views.view_user, name='user_view'),
    path('add-user/', views.create_user_view, name='add-user'),
]
