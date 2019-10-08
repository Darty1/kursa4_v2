from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseNotFound
# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic.edit import UpdateView

from .models import *
from django.utils import timezone


def index(request: HttpRequest):
    companys = Company.objects.all()
    categorys = Category.objects.all()
    return render(request, 'home.html', {'companys': companys, 'categorys': categorys})


def new(request, user_id):
    from .forms import Create_Company
    form = Create_Company(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        name = request.POST.get('name')
        price = request.POST.get('price')
        author_id = user_id
        date_of_end = request.POST.get('date_of_end')
        category_id = request.POST.get('category_id')
        description = request.POST.get('description')
        # image = request.FILES.get('image')
        image = request.POST.get('image')

        company = Company(name=name, price=price, author_id=author_id, date_of_end=date_of_end,
                          category_id=category_id, description=description, image=image)
        company.save()
        # users = User.objects.get(pk=user_id)
        # categorys = Category.objects.all()
        # companys = Company.objects.filter(author_id=users.id).values()
        # # return render(request, 'user.html', {'users': users, 'companys': companys, 'categorys': categorys})
        return redirect(reverse('index'))
    else:
        form = Create_Company()
        categorys = Category.objects.all()
    return render(request, 'new.html', {'form': form, 'error': True, 'categorys': categorys})


def add_bonus(request, company_id):
    from .forms import CreateBonus
    form = CreateBonus()
    categorys = Category.objects.all()
    if request.method == 'POST':
        print('i save')
        print('its valid')
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description_of_bonus')
        date = request.POST.get('date')
        company_id = company_id
        bonus = Bonus(name=name, price=price, description_of_bonus=description,
                          date=date, company_id=company_id)
        bonus.save()
        # company = Company.objects.get(id=company_id)
        return redirect(reverse('index'))
            # return render(request, 'add_bonus.html', {'categorys': categorys,  'form': form})
    else:
        form = CreateBonus()
    return render(request, 'add_bonus.html', {'categorys': categorys, 'form': form})


def logout(request: HttpRequest):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse('index'))


class Show(View):
    def get(self, request, category_id):
        companys = Company.objects.filter(category_id=category_id)
        categorys = Category.objects.all()
        return render(request, 'show.html', {'companys': companys, 'categorys': categorys})


class Show_all(View):
    def get(self, request):
        companys = Company.objects.all()
        categorys = Category.objects.all()
        return render(request, 'show.html', {'companys': companys, 'categorys': categorys})


class User_view(View):
    def get(self, request, user_id):
        users = User.objects.get(pk=user_id)
        categorys = Category.objects.all()
        companys = Company.objects.filter(author_id=users.id).values()
        support_companys = Consumer.objects.get(user_id=user_id)
        return render(request, 'user.html', {'users': users, 'companys': companys,
                                             'support_companys': support_companys,
                                            'categorys': categorys})


class Show_Company(View):
    def get(self, request, company_id: int):
        from django.db.models import ObjectDoesNotExist
        try:
            company = Company.objects.get(pk=company_id)
            bonuses = Bonus.objects.filter(company=company_id).values()
            categorys = Category.objects.all()
        except ObjectDoesNotExist:
            return HttpResponseNotFound
        day_of_end = timezone.timedelta(company.date_of_end.day)
        return render(request, 'company.html',
                      {'company': company, 'bonuses': bonuses, 'day_of_end': day_of_end, 'categorys': categorys})


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        from .forms import UserForm
        return render(request, 'registrable/login.html', {'form': UserForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User
        from .forms import UserForm
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user: User = authenticate(request, username=username, password=password)
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


def pay_st1(request, user_id, company_id):
    from .forms import PaidForm_st_1, PaidForm_st_2
    form = PaidForm_st_1(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            price = request.POST.get('price')
            user = User.objects.get(id=user_id)
            if Consumer.objects.filter(user_id=user_id):
                consumer = Consumer.objects.filter(user_id=user_id)
            else:
                consumer = Consumer.objects.create(user_id=user_id)
            consumer.wish_list.create(consumer_id=user_id, company_id=company_id)
            company = Company.objects.get(id=company_id)
            transaction = Transaction(user_id=user_id, company_id=company_id, price=price)
            transaction.save()
            categorys = Category.objects.all()
            form = PaidForm_st_2(request.POST)
            return render(request, 'pay_st_2.html', {'categorys': categorys, 'form': form, 'error': True,
                                                     'company': company, 'user': user})
        else:
            form = PaidForm_st_1()
    categorys = Category.objects.all()
    company = Company.objects.filter(id=company_id)
    user = User.objects.get(id=user_id)
    return render(request, 'pay_st_1.html',
                  {'form': form, 'categorys': categorys, 'company': company, 'user': user})


def pay_st2(request, user_id, company_id):
    from .forms import PaidForm_st_2
    categorys = Category.objects.all()
    company = Company.objects.get(id=company_id)
    return render(request, 'pay_st_2.html', {'form': PaidForm_st_2, 'categorys': categorys, 'company': company})


def pay_final(request, user_id, company_id):
    company = Company.objects.get(id=company_id)
    transaction = Transaction.objects.get(company_id=company_id, user_id=user_id)
    print('before company price = ', company.price)
    company.price -= transaction.price
    print('after company price = ', company.price)
    company.save()
    transaction.delete()
    return redirect(reverse('index'))


class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('index')


class CompanyUpdate(UpdateView):
    model = Company
    fields = ['name', 'price', 'image', 'description', 'date_of_end', 'category_id']
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('index')
