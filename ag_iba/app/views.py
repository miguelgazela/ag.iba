from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse


@login_required(login_url="login")
def index(request):
    return redirect('taxes')


def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request.POST)
        if request.POST and login_form.is_valid():
            user = login_form.login(request)
            if user:
                auth_login(request, user)
                return redirect('taxes')
            return render(request, 'app/auth/login.html',
                {'form': login_form})
        else:
            return HttpResponse(login_form.errors)
    else:
        return render(request, 'app/auth/login.html')


def logout(request):
    auth_logout(request)
    return redirect('index')


def signup(request):
    pass


@login_required(login_url="login")
def taxes(request, sort='all'):
    return render(request, 'app/taxes/list.html')