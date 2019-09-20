"""kursa4_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cashed import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
    path('company/<int:company_id>', views.Show.company, name='company'),
    path('show/company/<int:company_id>', views.Show.company, name='company'),
    path('user/company/<int:company_id>', views.Show.company, name='company'),
    path('user/<int:user_id>', views.Show.user_view, name='user'),
    path('show/company/pay_st_1', views.Paid_View.pay_st1, name='pay_st_1'),
    path('user/company/pay_st_1', views.Paid_View.pay_st1, name='pay_st_1'),
    path('show/company/pay_st_2', views.Paid_View.pay_st2, name='pay_st_2'),
    path('user/company/pay_st_2', views.Paid_View.pay_st2, name='pay_st_2'),
    path('show/<int:category_id>', views.Show.show, name='show'),
    path('user/show/', views.Show.show, name='show'),
    path('show/', views.Show.show_all, name='show'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)