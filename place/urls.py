from django.contrib import admin
from django.urls import path

from place.views import PostDetailView
app_name='place'

urlpatterns = [
    path('post/<int:pk>', PostDetailView.as_view(), name='post' ),
]


