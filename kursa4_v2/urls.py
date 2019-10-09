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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from cashed import views
from django.utils.translation import gettext_lazy as _
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    re_path(r'logout/$', views.logout, name='logout'),
    re_path(r'^(\w+/)*company/(?P<company_id>\d+)/$', views.Show_Company.as_view(), name='company'),
    re_path(r'user/(?P<user_id>\d+)/$', views.User_view.as_view(), name='user'),
    re_path(r'^(?P<user_id>\d+)/(?P<company_id>\d+)/pay_st_1/$', views.pay_st1, name='pay_st_1'),
    re_path(r'^(?P<user_id>\d+)/(?P<company_id>\d+)/pay_st_1/pay_st_2/$', views.pay_st2, name='pay_st_2'),
    re_path(r'^(?P<user_id>\d+)/(?P<company_id>\d+)/pay_final/$', views.pay_final, name='pay_final'),
    re_path(r'user/(?P<user_id>\d+)/new/$', views.new, name='new'),
    re_path(r'show/(?P<category_id>\d+)/$', views.Show.as_view(), name='show'),
    path('show_all/', views.Show_all.as_view(), name='show_all'),
    re_path(r'user_update/(?P<pk>\d+)/$', views.UserUpdate.as_view(), name='user_update'),
    re_path(r'company_update/(?P<pk>\d+)/$', views.CompanyUpdate.as_view(), name='company_update'),
    re_path(r'(?P<company_id>\d+)/add_bonus/$', views.add_bonus, name='add_bonus'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
