from utils import build_error_msg, build_success_msg

from place.models import Category, Place, Comment

class PostService():
    @staticmethod
    def find_by_category(category_pk):
        return Place.objects.filter(category__pk=category_pk)