from Demos.win32ts_logoff_disconnected import username
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_protect

from users.form import RegisterUserForm


@csrf_protect
def login_user(request):
    if request.user.is_authenticated:
        return redirect('transactions')

    if request.method == 'POST':
        user_name = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # Validate input
        if not user_name or not password:
            messages.error(request, 'Username and password are required.')
            return redirect('login')

        # Check if the username exists
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('login')

        # check if the user is activated
        if not user.is_active:
            messages.error(request, 'Your account is not active. Please contact support.')
            return redirect('login')

        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('transactions')
        else:
            messages.success(request, 'Incorrect password. Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('transactions')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user_date = form.save(commit=False)
            user_date.is_active = False
            user_date.save()
            return render(request, 'inactive-users.html')
        else:
            print(f'form result: {form}')
            return render(request, 'register.html', {'form': form})

    form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})
