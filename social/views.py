from place.services import PostService
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from place.models import Category
from place.services import PostService
# Create your views here.

# class IndexView(TemplateView):
#     template_name = "index.html"

class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'index.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['posts'] = PostService.get_all_posts()
        return context
