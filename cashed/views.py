from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
# Create your views here.
from django.urls import reverse
from django.views import View
from .models import *


def index(request: HttpRequest):
    companys = Company.objects.all()
    return render(request, 'home.html', {'companys': companys})


def user_view(request):
    users = User.objects.get(pk=request.user.id)
    return render(request, 'user.html', {'users': users})


def logout(request: HttpRequest):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse('index'))


def show(request):
    companys = Company.objects.all()
    return render(request, 'show.html', {'companys': companys})


def company(request: HttpRequest, company_id: int):
    from django.db.models import ObjectDoesNotExist
    try:
        company = Company.objects.get(pk=company_id)
        bonuses = Bonus.objects.all()
    except ObjectDoesNotExist:
        return Http404()
    return render(request, 'company.html', {'company': company, 'bonuses': bonuses})


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        from .forms import UserForm
        return render(request, 'registrable/login.html', {'form': UserForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User
        from .forms import UserForm

        form = UserForm(request.POST)
        if not form.is_valid():
            return render(request, 'registrable/login.html', {'form': UserForm(), 'error': True})
        user: User = authenticate(request, username=form.username, password=form.password)
        # if not user:
        #     return render(request, 'registrable/login.html', {'form': UserForm(), 'error': True})
        login(request, user)
        return redirect('index')


class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        from .forms import UserForm
        return render(request, 'registrable/register.html', {'form': UserForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        from django.contrib.auth import login
        from .models import Consumer
        from .forms import UserForm

        form = UserForm(request.POST)
        if not form.is_valid():
            return render(request, 'registrable/register.html', {'form': UserForm(), 'error': True})
        try:
            username = form.data['username']
            password = form.data['password']
            user = Consumer.objects.create_user(username, password=password)
        except:
            return render(request, 'registrable/register.html', {'form': UserForm(), 'error': True})
        login(request, user)
        return redirect(reverse('index'))
