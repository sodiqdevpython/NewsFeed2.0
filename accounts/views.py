from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm, CustomSignUpForm, SavePasswordForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from .models import ProfileModel


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('form is not valid')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form
    }

    return render(request, 'auth/password_change.html', context)


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return HttpResponse('Wrong username or password')
        else:
            print(form.errors)
            return HttpResponse('Form is not valid')
    else:
        form = CustomLoginForm()

    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)


def register_view(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        save_password_form = SavePasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            new_user_password = save_password_form.save(commit=False)
            new_user_password.username = data['username']
            new_user_password.password = data['password1']
            new_user_password.save()
            ProfileModel.objects.create(user=form.save())
            new_user = authenticate(request, username=data['username'], password=data['password1'])
            login(request, new_user)
            return redirect('profile')
        else:
            # print(form.errors)
            return HttpResponse('Form is not valid')
    else:
        form = CustomSignUpForm()

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)


@login_required
def update_profile(request):
    which_profile = ProfileModel.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=which_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = UpdateProfileForm(instance=which_profile)

    context = {
        'form': form
    }

    return render(request, 'profile_edit.html', context)
