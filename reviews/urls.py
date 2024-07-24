from django.urls import path
from .views import RestaurantReviewsView, ReviewListCreate, ReviewDetail

urlpatterns = [
    path('', ReviewListCreate.as_view(), name='review-list-create'),
    path('<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('restaurant/<int:pk>/', RestaurantReviewsView.as_view(), name='restaurant-review-detail'),
    
]
