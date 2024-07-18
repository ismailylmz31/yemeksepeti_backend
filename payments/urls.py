from django.urls import path
from .views import PaymentDetail

urlpatterns = [
    path('<int:pk>/', PaymentDetail.as_view(), name='payment-detail'),
]
