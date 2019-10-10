from django.forms import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': ('Name'),
            'email': ('Email'),
        }
        error_messages = {
            'username': {
                'max_length': ("This user's name is too long.")
            }
        }
        widgets = {
            'username': TextInput({'class': 'form-control'}),
            'email': EmailInput({'class': 'form-control'}),
            'password': PasswordInput({'class': 'form-control'})
        }
    username_validator = User.username_validator


class PaidForm_st_1(ModelForm):
    class Meta:
        model = Transaction
        fields = ['price']
        widgets = {
            'price': NumberInput({'class': 'form-control'})
        }

class PaidForm_st_2(Form):
    FirstName = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control'}))
    LastName = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control'}))
    S = CharField(min_length=9, widget=TextInput({'class': 'form-control'}))
    Card_Number = CharField(min_length=16, max_length=16, widget=TextInput({'class': 'form-control'}))
    Month = IntegerField(min_value=1, max_value=12, widget=TextInput({'class': 'form-control'}))
    Year = IntegerField(min_value=2015, max_value=2021, widget=TextInput({'class': 'form-control'}))
    CV = IntegerField(min_value=100, widget=TextInput({'class': 'form-control'}), max_value=999)


class Create_Company(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'category_id', 'date_of_end', 'price', 'image']
        labels = {
            'name': ('Name'),
            'date_of_end': ('Date of end'),
            'category_id': ('Category')
        }
        widgets = {
            'name': TextInput({'class': 'form-control', 'size': 8}),
            'description': TextInput({'class': 'form-control'}),
            'date_of_end': DateInput({'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'price': NumberInput({'class': 'form-control'}),
            # 'image': FileInput({'class': 'form-control'}),
        }
    image = ImageField()
    category_id = MultipleChoiceField(required=False, choices=(('1', 'Arts'), ('2', 'Comics'), ('3', 'Tech'),
                                                               ('4', 'Film'), ('5', 'Food'), ('6', 'Games'),
                                                               ('7', 'Music'), ('8', 'Publishing')),
                                 widget=SelectMultiple({'class': 'form-control'}))


class CreateBonus(ModelForm):
    class Meta:
        model = Bonus
        fields = ('name', 'price', 'description_of_bonus', 'date', 'img')
        widgets = {
            'name': TextInput({'class': 'form-control', 'size': 8}),
            'description_of_bonus': TextInput({'class': 'form-control'}),
            'date': DateInput({'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'price': NumberInput({'class': 'form-control'}),
        }