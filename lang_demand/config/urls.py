"""config URL Configuration

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),  # http://localhost:8000/ 뒤에 admin/붙으면 admin.site.urls 실행(장고에서 만든사이트)
    path('polls/', include('polls.urls')),  # http://localhost:8000/뒤에 polls/가 붙으면 polls 밑에 url를 실행
    path('stats/', include('stats.urls')),
    path('board/', include('board.urls')),
]
