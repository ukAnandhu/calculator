from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('calculate/', views.calculate, name='calculate'),
]