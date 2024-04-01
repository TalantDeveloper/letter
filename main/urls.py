from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('today/', views.today_view, name='today'),
    path('finish/', views.finish_view, name='finish'),
    path('timeout/', views.manager_out_view, name='timeout')
]

