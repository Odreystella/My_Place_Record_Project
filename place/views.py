from django.shortcuts import render, redirect
from django.views import View, generic

from place.models import Category
from place.services import PostService

# Create your views here.
class PostDetailView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'place_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostService.find_by_category(self.kwargs['pk'])
        return context