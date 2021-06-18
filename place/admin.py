from django.contrib import admin
from place.models import Category, Tag, Place, Photo, Comment


# Photo 클래스를 inline으로 나타낸다
class PhotoInline(admin.TabularInline):
    model = Photo

# Place 클래스는 해당하는 Photo 객체를 리스트로 관리한다.
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PhotoInline,]

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Place, PlaceAdmin)
# admin.site.register(Photo)
admin.site.register(Comment)