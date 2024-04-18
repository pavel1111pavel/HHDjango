from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url', 'named_url')
    list_filter = ('parent',)
    search_fields = ('title',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        print(queryset)  # Выводит queryset в консоль
        return queryset

admin.site.register(MenuItem, MenuItemAdmin)

