from django.db import models
from django.contrib.auth.models import User
from behaviors import BaseField
# Create your models here.

class Profile(BaseField):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=64)
    # selfie = models.ImageField(upload_to='image/', blank=True, null=True)