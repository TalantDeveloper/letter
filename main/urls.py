from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login_view, name='login'),

    path('welcome/', views.welcome, name='welcome'),
]

