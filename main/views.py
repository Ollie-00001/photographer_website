from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def services(request):
    return render(request, 'main/services.html')

def testimonials(request):
    return render(request, 'main/testimonials.html')

def contacts(request):
    return render(request, 'main/contacts.html')