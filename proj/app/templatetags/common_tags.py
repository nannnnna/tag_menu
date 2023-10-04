from django import template
from app.models import Menu
register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_top_menu(context):
    menu_items = Menu.objects.all()
    return {
        "menu_items": menu_items,
    } 
    
from django import template
from core.models import MenuItem
register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def show_menu(context):
    menu_items = MenuItem.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }

from django.urls import resolve

@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, menu_name='default'):
    current_path = context['request'].path
    current_url_name = resolve(current_path).url_name
    menu_items = MenuItem.objects.filter(menu__name=menu_name)

    # Выделение активного пункта меню
    for item in menu_items:
        item.is_active = False
        if item.url_name == current_url_name:
            item.is_active = True

    return {
        "menu_items": menu_items,
    }