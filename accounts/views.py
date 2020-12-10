from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from accounts.forms import UserForm, UserProfileForm, LoginForm


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

            # to do -> redirect to user profile page
            return redirect('index')

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
                # to do -> redirect to user profile
                return redirect('index')

        context = {
            'login_form': login_form,
        }

        return render(request, 'accounts/signin.html', context)


@login_required
def signout_user(request):
    logout(request)
    return redirect('index')
