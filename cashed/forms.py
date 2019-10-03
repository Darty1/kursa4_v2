from django.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class UserForm(Form):
    username_validator = User.username_validator
    username = CharField(min_length=3, max_length=32, validators=[username_validator], widget=TextInput({'class': 'form-control'}))
    email = EmailField(min_length=5, max_length=20, widget=EmailInput({'class': 'form-control'}))
    password = CharField(min_length=3, max_length=32, widget=PasswordInput({'class': 'form-control'}))


class PaidForm_st_1(Form):
    count = DecimalField()


class PaidForm_st_2(Form):
    FirstName = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control'}))
    LastName = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control'}))
    S = CharField(min_length=9, widget=TextInput({'class': 'form-control'}))
    Card_Number = CharField(min_length=16, max_length=16, widget=TextInput({'class': 'form-control'}))
    Month = IntegerField(min_value=1, max_value=12, widget=TextInput({'class': 'form-control'}))
    Year = IntegerField(min_value=2015, max_value=2021, widget=TextInput({'class': 'form-control'}))
    CV = IntegerField(min_value=100, widget=TextInput({'class': 'form-control'}), max_value=999)




class Create_Company(Form):
    name = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control', 'size': 8}))
    description = CharField(widget=TextInput({'class': 'form-control'}))
    category_id = MultipleChoiceField(required=False, choices=(('1', 'Arts'), ('2', 'Comics'), ('3', 'Tech'),
                                                               ('4', 'Film'), ('5', 'Food'), ('6', 'Games'),
                                                               ('7', 'Music'), ('8', 'Publishing')),
                                 widget=SelectMultiple({'class': 'form-control'}))
    date_of_end = DateField(input_formats=['%Y/%m/%d'], widget=DateInput({'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}))
    price = DecimalField(widget=NumberInput({'class': 'form-control'}))
    image = FileField(widget=FileInput({'class': 'form-control'}))