from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin





class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active','role')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active'),
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role', {'fields': ('role',)}),
    )

admin.site.register(User, BaseUserAdmin)