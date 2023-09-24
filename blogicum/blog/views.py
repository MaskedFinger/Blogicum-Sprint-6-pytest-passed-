from blog.models import Category, Post
from django.shortcuts import get_object_or_404, render
from django.utils import timezone


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        is_published=True,
        category__is_published=True,
        pk=post_id,
        pub_date__lte=timezone.now()
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=slug,
    )
    post_list = Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
