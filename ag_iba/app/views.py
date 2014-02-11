from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.http import Http404
from app.forms import UserCreationForm
from app.forms import ClientForm
from app.forms import TaxForm
from app.models import Client
from app.models import Tax

import json
from datetime import timedelta


@login_required
def index(request):
    return redirect('taxes')

# Auth Views -->

def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if request.POST and login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('taxes')
        else:
            return render(request, 'app/auth/login.html',
                {'form': login_form})
    elif request.method == 'GET':
        return render(request, 'app/auth/login.html')


@login_required
def logout(request):
    """
    Log users out and re-direct them to the main page.
    """
    auth_logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'GET':
        return render(request, 'app/auth/signup.html')
    elif request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user = user_form.save(commit=False)
            user.is_active = False
            user.save()
            return render(request, 'app/auth/signup.html',
                {'username': username, 'status': 'success'})
        else:
            return render(request, 'app/auth/signup.html',
                {'form': user_form})


# <-- /. Auth Views


# Taxes Views -->


@login_required
def taxes(request, sort='all'):

    if not request.user.is_superuser:
        taxes = Tax.objects.all().filter(client__from_home=False)\
            .order_by('limit_date')
    else:
        valid_sorting = ['all', 'home', 'office']
        if not sort in valid_sorting:
            sort = 'all'

        if sort == 'all':
            taxes = Tax.objects.all().order_by('limit_date')
        else:
            taxes = Tax.objects.all().filter(client__from_home=(sort == 'home'))\
                .order_by('limit_date')

    return render(request, 'app/taxes/list.html',
        {'list_taxes': taxes, 'sort': sort})


@login_required
def add_tax(request, client_id=None):

    if client_id is not None:
        client = get_object_or_404(Client, pk=client_id)
        if not request.user.is_superuser and client.from_home:
            raise Http404
        clients = [(client.name, client.id)]
    else:
        if not request.user.is_superuser:
            clients = Client.objects\
                .extra(select={'lower_name':'lower(name)'})\
                .filter(from_home=False)\
                .order_by('lower_name')\
                .values_list('name', 'id')
        else:
            clients = Client.objects\
                .extra(select={'lower_name':'lower(name)'})\
                .order_by('lower_name')\
                .values_list('name', 'id')

    if request.method == 'GET':
        return render(request, 'app/taxes/add.html',
            {'list_clients': clients})
    else:
        tax_form = TaxForm(request.POST)
        if tax_form.is_valid():
            tax_form.save()
            return render(request, 'app/taxes/add.html',
                {'status': 'success'})
        else:
            return render(request, 'app/taxes/add.html',
                {'form': tax_form, 'list_clients': clients, 'status': 'fail'})

# <-- /. Taxes Views


# Clients Views -->


@login_required
def clients(request, sort='all'):

    if not request.user.is_superuser:
        clients = Client.objects.all().filter(from_home=False)\
            .order_by('name')
    else:
        valid_sorting = ['all', 'home', 'office']
        if not sort in valid_sorting:
            sort = 'all'

        if sort == 'all':
            clients = Client.objects.all().order_by('name')
        else:
            clients = Client.objects.all().filter(from_home=(sort == 'home'))\
                .order_by('name')

    return render(request, 'app/clients/list.html',
        {'list_clients': clients, 'sort': sort})


@login_required
def client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    taxes = client.tax_set.all().order_by('limit_date')
    return render(request, 'app/clients/view.html',
        {'client': client, 'taxes': taxes })


@login_required
def add_client(request):
    if request.method == 'GET':
        return render(request, 'app/clients/add.html')
    elif request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client = client_form.save(commit=False)
            client.from_home = request.POST.get('client_type') == 'home'
            client.save()
            return redirect('client', client_id=client.id)
        else:
            return render(request, 'app/clients/add.html',
                {'form': client_form})


# <-- /. Clients Views


# API Views -->

def pay_tax(request, tax_id):
    """Adds a year to the limit date of a tax"""

    return change_tax(request, tax_id, timedelta(days=365))


def cancel_tax(request, tax_id):
    """Subtracts a year to the limit date of a tax"""

    return change_tax(request, tax_id, - timedelta(days=365))


def change_tax(request, tax_id, time_change):
    response = {'status': 'fail', 'data': None}

    if request.is_ajax() and request.user.is_authenticated():
        try:
            tax = Tax.objects.get(pk=tax_id)
            tax.limit_date = tax.limit_date + time_change
            tax.save()
            response['status'] = 'success'
        except Tax.doesNotExist:
            response['data'] = {'title': 'No Tax with that id was found'}
    else:
        response['data'] = {'title': "API can only be used with authenticated AJAX requests"}

    return HttpResponse(
        json.dumps(response, cls=DjangoJSONEncoder),
        content_type="application/json")


