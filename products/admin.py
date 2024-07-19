from django.contrib import admin
from .models import Category,Product
# Regist    er your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price', 'category')
    search_fields = ('name', 'restaurant__name')
    list_filter = ('category', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
