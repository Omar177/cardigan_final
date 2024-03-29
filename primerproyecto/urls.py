"""primerproyecto URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views


urlpatterns = [
url(r'^admin/',admin.site.urls),
url(r'^App1/',include(('Apps.Aplicacion1.urls','app1'), namespace='app1')),
url(r'^App2/',include(('Apps.usuario.urls','app2'), namespace='app2')),
path('login/', LoginView.as_view(template_name='login.html'),name = 'login'),
    path('', LogoutView.as_view(), name='logout'),
 ]
