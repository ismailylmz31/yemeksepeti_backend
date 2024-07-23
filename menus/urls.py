from django.urls import path
from .views import MenuListCreate, MenuDetail, RestaurantMenusView

urlpatterns = [
    path('', MenuListCreate.as_view(), name='menu-list-create'),
    path('<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
    path('restaurant/<int:pk>/', RestaurantMenusView.as_view(), name='restaurant-menus'),
]
