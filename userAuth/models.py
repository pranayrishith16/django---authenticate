from django.db import models
<<<<<<< Updated upstream
=======
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
>>>>>>> Stashed changes

from .managers import CustomUserManager


class AuthUser(AbstractUser): #( Abstract User is used to use existing User model and remove username field )
    username = None
    email = models.EmailField(unique=True, help_text='Email Address')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    
# class AuthUser(AbstractBaseUser): #( Creating an User model from scratch )
#     email = models.EmailField(help_text='Email address', unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email