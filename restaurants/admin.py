from django.contrib import admin
from .models import Offer, Restaurant
# Register your models here.




class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'address', 'created_at','rating','min_basket_price','delivery_price','delivery_time')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at',)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_exist', 'restaurant')
    search_fields = ('title', 'description')
    list_filter = ('is_exist',)

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Offer,OfferAdmin)