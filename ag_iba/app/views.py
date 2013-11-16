from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


@login_required
def index(request):
    return HttpResponse("This will be the taxes index")


def login(request):
    if request.method == 'POST':
        return HttpResponse('Trying to login')
    else:
        return render(request, 'app/login.html')