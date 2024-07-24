from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Menu
from .serializers import MenuSerializer

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer    

    def perform_create(self, serializer):
        restaurant = self.request.data.get('restaurant')
        serializer.save(restaurant_id=restaurant)

    search_fields = ['name', 'description']
    ordering_fields = ['name',]    

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class RestaurantMenusView(generics.ListAPIView):  
    def get_queryset(self):
        restaurant_id = self.kwargs['pk']
        return Menu.objects.filter(restaurant_id=restaurant_id)
    
    search_fields = ['name', 'description']
    ordering_fields = ['name',]  

    serializer_class = MenuSerializer
