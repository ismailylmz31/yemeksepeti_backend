
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/restaurants/', include('restaurants.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/menus/', include('menus.urls')), 
    path('api/products/', include('products.urls')), 
    path('api/tracking/', include('tracking.urls')), 
    path('api/payments/', include('payments.urls')),
    path('api/profiles/', include('profiles.urls')),
   
]
