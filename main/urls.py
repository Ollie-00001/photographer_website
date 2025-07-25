from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contacts/', views.contacts, name='contacts'),
]