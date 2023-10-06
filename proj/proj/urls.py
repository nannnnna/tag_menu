from django.contrib import admin
from django.urls import path, include
from app.views import base_view, first_view, menu_view, second_view, third_view
from core.views import core_menu_view
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_view, name='base'),
    path('menu/', menu_view, name='menu'),
    path('core_menu/', core_menu_view, name='core_menu'),
    path('first/', first_view, name='first'),
    path('second/', second_view, name='second'),
    path('third/', third_view, name='third'),
]
