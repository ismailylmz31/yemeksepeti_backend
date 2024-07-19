from django.contrib import admin
from .models import Menu,MenuItem
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')
    search_fields = ('name', 'restaurant__name')
    

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem)


