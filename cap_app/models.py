from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    mobile = models.CharField(max_length=15, blank=False, null=False)
    
    # Other fields from AbstractUser like username, password, etc., are already included.

    def __str__(self):
        return self.username
