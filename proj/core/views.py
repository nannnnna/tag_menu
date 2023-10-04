from django.shortcuts import render

def core_menu_view(request):
    return render(request, 'templatetags/menu.html')
