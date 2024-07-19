from django.contrib import admin
from .models import Restaurant
# Register your models here.




class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at',)

admin.site.register(Restaurant,RestaurantAdmin)