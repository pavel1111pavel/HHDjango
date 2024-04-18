from django.shortcuts import render
from .models import MenuItem

def menu_page(request):
    menu_items = MenuItem.objects.filter(parent=None).prefetch_related('children')
    return render(request, 'menu_page.html', {'menu_items': menu_items})


