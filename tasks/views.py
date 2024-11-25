from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser

def home_view(request):
    """Vista para la página principal."""
    return render(request, 'tasks/index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account_details')
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/create.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('account_details')
    else:
        form = UserLoginForm()
    return render(request, 'tasks/login.html', {'form': form})

@login_required
def account_details(request):
    return render(request, 'tasks/detail.html', {'user': request.user})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('account_details')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'tasks/change_password.html', {'form': form})

@login_required
def delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'tasks/delete.html', {'user': request.user})
