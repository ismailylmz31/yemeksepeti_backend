from django.urls import path
from .views import OrderStatusDetail

urlpatterns = [
    path('<int:pk>/', OrderStatusDetail.as_view(), name='order-status-detail'),
]
