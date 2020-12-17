from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.translator,name='translator'),
    path('translated/', views.translated, name='translated')

]