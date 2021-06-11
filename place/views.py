from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib import messages

from place.models import Category, Place
from place.services import PostService
from place.dto import CreateDto, UpdateDto

# Create your views here.
class CategoryDetailView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'place_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostService.find_by_post(self.kwargs['pk'])
        return context

class PostDetailView(generic.DetailView):
    model = Place
    context_object_name = 'post'
    template_name = 'place_detail.html'


class PostCreateView(View):
    def get(self, request, *args, **kwargs):
        category_pk = self.kwargs['pk']
        category = PostService.find_by_category(category_pk)
        context = {'category' : category}
        return render(request, 'place_add.html', context)

    def post(self, request, *args, **kwargs):
        category_pk = self.kwargs['pk']
        create_dto = self._build_add_dto(request)
        result = PostService.create(create_dto)
        context = { 'error' : result['error']}
        if result['error']['status']:
            return render(request, 'place_add.html', context)
        return redirect('place:post', category_pk)

    def _build_create_dto(self, request):
        category = PostService.find_by_category(self.kwargs['pk'])
        return CreateDto(
            category=category,
            author=request.user,
            name=request.POST['name'],
            location=request.POST['location'],
            memo=request.POST['memo'],
            best_menu=request.POST['best_menu'],
            additional_info=request.POST['additional_info'],
            stars=request.POST['stars'],
            # tag=request.POST['tag'],
            image=request.FILES.getlist('image'),
            pk=self.kwargs['pk'],
        )

class PostUpdateView(View):
    success_message = '게시글이 수정되었습니다.'

    def get(self, request, *args, **kwargs):
        post_pk = self.kwargs['pk']
        post = PostService.get_post(post_pk)
        context = {'post' : post}
        return render(request, 'place_edit.html', context)

    def post(self, request, *args, **kwargs):
        post_pk = self.kwargs['pk']
        post = PostService.get_post(post_pk)

        update_dto = self._build_update_dto(request)
        result = PostService.update(update_dto)

        if len(messages.get_messages(request)) == 0:
            messages.success(self.request, self.success_message)
        # messages.error(self.request, '알 수 없는 요청입니다.')

        print(result)
        context = {'post' : post, 'error' : result['error']}
        if result['error']['status']:
            return render(request, 'place_edit.html', context)
        return redirect('place:detail', post_pk)

    def _build_update_dto(self, request):
        return UpdateDto(
            name=request.POST['name'],
            location=request.POST['location'],
            stars=request.POST['stars'],
            memo=request.POST['memo'],
            best_menu=request.POST['best_menu'],
            additional_info=request.POST['additional_info'],
            image=request.FILES.getlist('image'),
            pk=self.kwargs['pk']
        )
