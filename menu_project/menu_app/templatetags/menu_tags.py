from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent=None)
    return render_menu(menu_items)

def render_menu(menu_items):
    html = '<ul>'
    for item in menu_items:
        html += '<li><a href="{}">{}</a>'.format(item.url or item.named_url, item.title)
        if item.children.exists():
            html += render_menu(item.children.all())
        html += '</li>'
    html += '</ul>'
    return html

