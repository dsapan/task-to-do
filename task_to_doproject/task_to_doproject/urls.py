"""task_to_doproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from task_to_doapp.views import home,createtask
from authapp.views import usignup,ulogin,ulogout,uforgotpass,uchangepass

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',home,name='home'),
    path('usignup/',usignup,name='usignup'),
    path('ulogin/',ulogin,name='ulogin'),
    path('ulogout/',ulogout,name='ulogout'),
    path('ufogotpass/',uforgotpass,name='uforgotpass'),
    path('uchangepass/',uchangepass,name='uchangepass'),
    path('createtask/',createtask,name='createtask'),
 

]
