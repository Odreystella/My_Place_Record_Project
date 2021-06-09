from dataclasses import dataclass
from place.models import Category
from django.contrib.auth.models import User


@dataclass
class AddDto():
    category : Category
    author : User 
    name : str
    location : str
    memo : str
    best_menu : str
    additional_info : str
    stars : str
    # tag : str
#    image : str 
    pk : str