from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def register(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'registerform': form}

    return render(request, 'registration.html', context=context)


def login(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'loginform': form}

    return render(request, 'login.html', context=context)


def user_logout(request):
    auth.logout(request)

    return redirect("catalog")


@login_required(login_url="login")
def dashboard(request):
    return render(request, 'dashboard.html')


def catalog(request):
    return render(request, 'catalog.html')
