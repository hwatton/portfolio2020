from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def pagetwo(request):
    return render(request, 'pagetwo.html', {})

def about(request):
    return render(request, 'about.html', {})

def graphics(request):
    return render(request, 'graphics.html', {})
