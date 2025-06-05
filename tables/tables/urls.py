"""
URL configuration for Dept project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dept_view/', dept_view, name='dept_view'),
    path('insert_emp/', insert_emp, name='insert_emp'),
    path('diplay_Dept/', diplay_Dept, name='diplay_Dept'),
    path('diplay_emp/', diplay_emp, name='diplay_emp'),
    path('joins/', joins, name='joins'),
    path('selfjoin/', selfjoin, name='selfjoin'),
    path('emd/', emd, name='emd'),

]
