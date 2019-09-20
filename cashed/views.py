from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
# Create your views here.
from django.urls import reverse
from django.views import View
from .models import *
from django.utils import timezone


def index(request: HttpRequest):
    companys = Company.objects.all()
    categorys = Category.objects.all()
    return render(request, 'home.html', {'companys': companys, 'categorys': categorys})


def logout(request: HttpRequest):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse('index'))


class Show(View):
    def show(request, category_id: int):
        companys = Company.objects.filter(category_id=category_id)
        categorys = Category.objects.all()
        return render(request, 'show.html', {'companys': companys, 'categorys': categorys})

    def show_all(request):
        companys = Company.objects.all
        categorys = Category.objects.all()
        return render(request, 'show.html', {'companys': companys, 'categorys': categorys})

    def company(request: HttpRequest, company_id: int):
        from django.db.models import ObjectDoesNotExist
        try:
            company = Company.objects.get(pk=company_id)
            bonuses = Bonus.objects.filter(company=company_id).values()
            categorys = Category.objects.all()
        except ObjectDoesNotExist:
            return Http404()
        day_of_end = timezone.timedelta(company.date_of_end.day)
        return render(request, 'company.html',
                      {'company': company, 'bonuses': bonuses, 'day_of_end': day_of_end, 'categorys': categorys})

    def user_view(request, user_id: int):
        users = User.objects.get(pk=user_id)
        categorys = Category.objects.all()
        companys = Company.objects.filter(author_id=users.id).values()
        return render(request, 'user.html', {'users': users, 'companys': companys, 'categorys': categorys})


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        from .forms import UserForm
        return render(request, 'registrable/login.html', {'form': UserForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User
        from .forms import UserForm
        form = UserForm(request.POST)

        user: User = authenticate(request, username=form.username, password=form.password)
        if not user:
            return render(request, 'home.html', {'form': UserForm(), 'error': True})
        login(request, user)
        return redirect(reverse('index'))


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
            user = User.objects.create_user(username=username, password=password)
        except:
            return render(request, 'registrable/register.html', {'form': UserForm(), 'error': True})
        login(request, user)
        return redirect(reverse('index'))


class Paid_View(View):
    def pay_st1(request):
        from .forms import PaidForm_st_1
        categorys = Category.objects.all()
        return render(request, 'pay_st1.html', {'form': PaidForm_st_1(), 'categorys': categorys})

    def pay_st2(request):
        from .forms import PaidForm_st_2
        categorys = Category.objects.all()
        return render(request, 'pay_st_2.html', {'form': PaidForm_st_2(), 'categorys': categorys})
