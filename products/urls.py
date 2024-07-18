from django.urls import path
from .views import CategoryListCreate, CategoryDetail, ProductListCreate, ProductDetail

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('', ProductListCreate.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
