from django.contrib import admin
from django.urls import path

from place.views import PostDetailView, PostAddView
app_name='place'

urlpatterns = [
    path('post/<int:pk>', PostDetailView.as_view(), name='post' ),
    path('post/add/<int:pk>', PostAddView.as_view(), name='post-add' ),
]


