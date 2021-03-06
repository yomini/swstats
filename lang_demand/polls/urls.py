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
from django.urls import path
from . import views

app_name = "polls"  # 이름 충돌 방지 위해 앱이름 공간 지정

urlpatterns = [
    path('', views.vote, name="vote"),  # http://localhost:8000/polls/ 뒤에 아무것도 안나오면  views.py안의 list 실행해라
    path('list', views.list, name="list"),  # http://localhost:8000/polls/ 뒤에 아무것도 안나오면  views.py안의 list 실행해라

]
