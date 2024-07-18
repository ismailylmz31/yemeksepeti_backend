from django.urls import path
from .views import MenuListCreate, MenuDetail

urlpatterns = [
    path('', MenuListCreate.as_view(), name='menu-list-create'),
    path('<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
]
