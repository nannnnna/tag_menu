from django.shortcuts import render

def base_view(request):
    return render(request, 'base.html')

def menu_view(request):
    return render(request, 'menu.html')

def first_view(request):
    return render(request, 'first.html')

def second_view(request):
    return render(request, 'second.html')

def third_view(request):
    return render(request, 'third.html')
