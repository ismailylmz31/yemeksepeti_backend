from django.contrib import admin
from .models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant','rating')
    search_fields = ('user__username', 'restaurant__name', 'product__name')
    list_filter = ('rating',)


admin.site.register(Review, ReviewAdmin)
