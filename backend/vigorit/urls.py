from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'vigorit'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # {'template_name': 'vigorit/login.html'},
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # {'template_name': 'vigorit/logout.html', 'next_page': '/login'},
    path('logout/', views.user_logout, name='logout'),
    path('form/', views.data_form, name='form')
]
