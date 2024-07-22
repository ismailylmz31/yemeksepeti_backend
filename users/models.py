from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
    
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_groups',
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_permissions',
#         blank=True
#     )

#     def __str__(self):
#         return self.email


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    RESTAURANT_OWNER = 'restaurant_owner'
    CUSTOMER = 'customer'
    
    ROLE_CHOICES = [
        (RESTAURANT_OWNER, 'Restaurant Owner'),
        (CUSTOMER, 'Customer'),
    ]
    
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    
    def __str__(self):
        return self.email
        