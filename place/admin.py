from django.contrib import admin
from place.models import Category, Tag, Place, Photo, Comment
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Place)
admin.site.register(Photo)
admin.site.register(Comment)