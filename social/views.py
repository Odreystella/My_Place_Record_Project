from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from place.models import Category
# Create your views here.

# class IndexView(TemplateView):
#     template_name = "index.html"

class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'index.html'
