from django.urls import path

from . import views

app_name = 'vigorit'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    # path('delivery/', views.delivery, name='delivery'),
]
