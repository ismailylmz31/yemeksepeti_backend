from django.contrib import admin
from .models import Profile
# Register your models here.



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    search_fields = ('user__username', 'user__email', 'phone_number')
    

admin.site.register(Profile, ProfileAdmin)    