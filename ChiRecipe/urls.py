"""ChiRecipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include

from recipe import views, register

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', views.index, name='homepage'),

    url(r'account/', include([
        url(r'login', register.login, name='login'),
        url(r'logout', register.logout, name='logout'),
        url(r'register', register.user_register, name='register')
        # url(r'profile', register.profile, name='profile'),
        # url(r'edit/(?P<reg_id>[a-zA-Z0-9])+', register.edit_profile, name='edit_profile'),
        # url(r'forget_password', register.forget_password, name='forger_password'),
        # url(r'change_password', register.change_password, name='change_password'),
    ])),
]
