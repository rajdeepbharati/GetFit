from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from .forms import UserForm, AppUserForm
from .models import AppUser, Diet
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

import math
import random
import itertools

from django.contrib.auth.models import User


def calculate_bmi(appUser):
    bmi = (appUser.weight)/(math.pow(appUser.height, 2))
    appUser.bmi = round(bmi, 2)
    appUser.save()


def check_health(appUser):
    if appUser.bmi < 18.5:
        health = 'underweight'
    elif appUser.bmi >= 18.5 and appUser.bmi < 25:
        health = 'healthy'
    elif appUser.bmi >= 25 and appUser.bmi < 30:
        health = 'overweight'
    else:
        health = 'obese'
    appUser.health = health
    appUser.save()


@login_required(redirect_field_name='/login')
def index(request):
    # print(request.user)
    if request.user.is_authenticated:
        appUser = AppUser.objects.get(user=request.user)
        calculate_bmi(appUser)
        check_health(appUser)
        diets = Diet.objects.all()
        if appUser.health == 'healthy':  # and appUser.sex==1:
            recommend = 'maintain'
            if appUser.sex == 0:  # male
                calories = 2500
            else:  # woman
                calories = 2000
        elif appUser.health == 'underweight':
            recommend = 'eat more'
            if appUser.sex == 0:
                calories = 3000
            else:
                calories = 2500
        elif appUser.health == 'overweight' or appUser.health == 'obese':
            recommend = 'eat less'
            if appUser.sex == 0:
                calories = 2000
            else:
                calories = 1500
        # print(diets)
        recommendedDiets = Diet.objects.filter(calories=calories)
        # ids=set(rd.id for rd in recommendedDiets)
        # rds=filter(lambda x: x.id in ids, recommendedDiets)
        # recommendedDiets=rds
        print(recommendedDiets)
        rds=list(recommendedDiets)
        print(rds)
        v=rds[random.choice(range(recommendedDiets.count()))]
        print(v)
        context = {
            # 'username':appUser.username,
            'name': appUser.name,
            'bmi': appUser.bmi,
            'health': appUser.health,
            'recommend': recommend,
            'diets': diets,
            'sex': appUser.sex,
            'calories':calories,
            'recommendedDiet': v
        }
        print(appUser.name)
    else:
        print(request.user)
    return render(request, 'vigorit/index.html', context)


@login_required
def user_logout(request):
    logout(request)
    # return render(request, 'vigorit/login.html')
    return redirect('/login')
    # return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('vigorit.index')
    else:
        form = UserForm()
    return render(request, 'vigorit/registration.html', {'form': form})


# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         AppUser_form = AppUserForm(data=request.POST)
#         if user_form.is_valid():  # and AppUser_form.is_valid():
#             user = user_form.save(commit=False)
#             user.set_password(user.password)   # Is this neccesary ??
#             user.save()
#             # appUser = AppUser_form.save(commit=False)
#             # appUser.user_id = user

#             # appUser.save()
#             registered = True
#         else:
#             print(user_form.errors, AppUser_form.errors)
#     else:
#         user_form = UserForm()
#         AppUser_form = AppUserForm()
#     return render(request, 'vigorit/registration.html',
#                   {'user_form': user_form,
#                    #    'AppUser_form': AppUser_form,
#                    'registered': registered})


def user_login(request):
    loggedIn = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                loggedIn = True
                return redirect('/')
                # return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            loggedIn = False
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'vigorit/login.html', {'loggedIn': loggedIn})
