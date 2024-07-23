from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Offer, Restaurant
from .serializers import OfferSerializer, RestaurantSerializer


class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address', 'description']
    ordering_fields = ['name', 'rating']
    
    

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
    


class OfferListCreate(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    search_fields = ['title','is_exist','description']
    ordering_fields = ['title',]
   

class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    # permission_classes = [IsAuthenticated] ÜSTTEKİ CLASSLARDADA AUTHENTİCATİON OLMALI ÜŞENİP SİLDİM

class RestaurantOfferView(generics.ListAPIView):  
    def get_queryset(self):
        restaurant_id = self.kwargs['pk']
        return Offer.objects.filter(restaurant_id=restaurant_id)
    
    serializer_class = OfferSerializer    
