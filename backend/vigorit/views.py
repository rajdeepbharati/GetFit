from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from .forms import UserForm, AppUserForm
from .models import AppUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

import math

from django.contrib.auth.models import User


def calculate_bmi(appUser):
    bmi = (appUser.weight)/(math.pow(appUser.height, 2))
    appUser.bmi = round(bmi, 2)
    appUser.save()


@login_required
def index(request):
    # print(request.user)
    if request.user.is_authenticated:
        appUser = AppUser.objects.get(user=request.user)
        print(appUser.bmi)
        calculate_bmi(appUser)
        print(appUser.bmi)
        context = {
            'bmi': appUser.bmi
        }
    else:
        print(request.user)
    return render(request, 'vigorit/index.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        AppUser_form = AppUserForm(data=request.POST)
        if user_form.is_valid():  # and AppUser_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)   # Is this neccesary ??
            user.save()
            # appUser = AppUser_form.save(commit=False)
            # appUser.user_id = user

            # appUser.save()
            registered = True
        else:
            print(user_form.errors, AppUser_form.errors)
    else:
        user_form = UserForm()
        AppUser_form = AppUserForm()
    return render(request, 'vigorit/registration.html',
                  {'user_form': user_form,
                   #    'AppUser_form': AppUser_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/')
                # return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'vigorit/login.html', {})
