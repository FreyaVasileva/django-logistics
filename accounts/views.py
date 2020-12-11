import os

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from accounts.decorators import group_required
from accounts.forms import UserForm, UserProfileForm, LoginForm
from consignment.models import Consignment


def signup_user(request):
    if request.method == 'GET':
        context = {
            'user_form': UserForm(),
            'profile_form': UserProfileForm(),
        }

        return render(request, 'accounts/signup.html', context)
    else:
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            profile.save()

            login(request, user)

            return redirect('user profile')

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'accounts/signup.html', context)


def signin_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }
        return render(request, 'accounts/signin.html', context)
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('user profile')

        context = {
            'login_form': login_form,
        }

        return render(request, 'accounts/signin.html', context)


@login_required
def signout_user(request):
    logout(request)
    return redirect('index')


@login_required
def user_profile(request):
    user = request.user
    user_profile = user.userprofile
    consignments = Consignment.objects.filter(receiver_id=user.id).first()

    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user_profile,
            'consignments': consignments,
            'form': UserProfileForm(),
            'is_worker': user.groups.filter(name='worker').exists(),
            'is_customer': user.groups.filter(name='customer').exists(),
        }
        return render(request, 'accounts/user_profile.html', context)
    else:
        old_image = user_profile.profile_picture
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            if old_image:
                os.remove(old_image.path)
            form.save()
            return redirect('user profile')

        return redirect('user profile')


@group_required(['worker'])
def add_worker(request):
    if request.method == 'GET':
        context = {
            'user_form': UserForm(),
            'profile_form': UserProfileForm(),
            'is_worker': True,
        }

        return render(request, 'accounts/add_worker.html', context)
    else:
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            group = Group.objects.get(name='worker')
            user.groups.add(group)

            profile.save()
            return redirect('user profile')

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'is_worker': True,
        }
        return render(request, 'accounts/add_worker.html', context)