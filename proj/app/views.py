from django.shortcuts import render

def base_view(request):
    return render(request, 'base.html')

def menu_view(request):
    return render(request, 'menu.html')
