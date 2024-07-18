from django.urls import path
from .views import RestaurantListCreate, RestaurantDetail,CategoryListCreate, CategoryDetail, ProductListCreate, ProductDetail

urlpatterns = [
    path('', RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),

    
]