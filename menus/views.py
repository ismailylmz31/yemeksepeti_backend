from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Menu
from .serializers import MenuSerializer

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        restaurant = self.request.data.get('restaurant')
        serializer.save(restaurant_id=restaurant)

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
