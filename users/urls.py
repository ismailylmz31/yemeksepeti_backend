from django.urls import path
from .views import UserCreate, UserLogin, UserDetail

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
