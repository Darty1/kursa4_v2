from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(Company)
admin.site.register(Consumer)
admin.site.register(Bonus)
admin.site.register(Category)

