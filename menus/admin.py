from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'total_price')
    search_fields = ('name', 'restaurant__name')
    inlines = [MenuItemInline]

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem)
