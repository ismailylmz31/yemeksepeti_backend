from django.urls import path
from .views import OfferDetail, OfferListCreate, RestaurantListCreate, RestaurantDetail

urlpatterns = [
    path('', RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
    path('offers/', OfferListCreate.as_view(), name='offer-list-create'),
    path('offers/<int:pk>/', OfferDetail.as_view(), name='offer-detail'),
]
