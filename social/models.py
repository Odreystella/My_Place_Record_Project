from django.core.exceptions import BadRequest
from django.db import models
from django.contrib.auth.models import User
from behaviors import BaseField

# Create your models here.
class Relationship(BaseField):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='relationship')
    followers = models.ManyToManyField(User, blank=True, related_name='following')