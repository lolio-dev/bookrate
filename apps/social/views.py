import django.db.utils
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_htmx.http import HttpResponseClientRedirect

from apps.social.forms import LoginForm, SignupForm
from apps.social.models import User


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseClientRedirect("/")
            else:
                form.add_error(None, ValidationError('Invalid credentials'))
                return render(request, 'users/partials/login-form.html', {"form": form})
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {"form": form})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_validation']:
                try:
                    user = User.object.create_user(
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password'],
                        username=form.cleaned_data['username']
                    )
                except django.db.utils.IntegrityError:
                    form.add_error('email', ValidationError('User with this email already exsits'))
                    return render(request, 'users/partials/signup-form.html', {"form": form})

                login(request, user)
                return HttpResponseClientRedirect("/")
            else:
                form.add_error('password', ValidationError('Passwords missmatch'))
                form.add_error('password_validation', ValidationError('Passwords missmatch'))
                return render(request, 'users/partials/signup-form.html', {"form": form})
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {"form": form})


@login_required
def logout_view(request):
    logout(request)

    return HttpResponseRedirect("/")


@login_required
def settings_view(request):
    return render(request, 'users/settings.html')
