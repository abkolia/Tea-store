from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def catalog(request):
    return render(request, 'main/catalog.html')