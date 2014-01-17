from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url="login")
def index(request):
    return redirect('taxes')


def login(request):
    if request.method == 'POST':
        return HttpResponse('Trying to login')
    else:
        return render(request, 'app/login.html')


def logout(request):
    pass


def signup(request):
    pass


@login_required(login_url="login")
def taxes(request, sort='all'):
    return render(request, 'app/taxes/list.html')