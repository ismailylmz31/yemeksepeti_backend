from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import OrderStatus
from .serializers import OrderStatusSerializer

class OrderStatusDetail(generics.RetrieveUpdateAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    # permission_classes = [IsAuthenticated]
