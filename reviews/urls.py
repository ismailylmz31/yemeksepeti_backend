from django.urls import path
from .views import ReviewListCreate, ReviewDetail

urlpatterns = [
    path('', ReviewListCreate.as_view(), name='review-list-create'),
    path('<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
