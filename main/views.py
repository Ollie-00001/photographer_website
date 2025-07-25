from django.shortcuts import render
from .models import Page

def index(request):
    pages = Page.objects.all()
    return render(request, 'main/index.html', {'pages': pages})

def portfolio(request):
    pages = Page.objects.all()
    return render(request, 'main/portfolio.html', {'pages': pages})

def services(request):
    pages = Page.objects.all()
    return render(request, 'main/services.html', {'pages': pages})

def testimonials(request):
    pages = Page.objects.all()
    return render(request, 'main/testimonials.html', {'pages': pages})

def contacts(request):
    pages = Page.objects.all()
    return render(request, 'main/contacts.html',  {'pages': pages})