from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *


def index_view(request):
    posts = Post.objects.filter(is_published=True)
    d = {
        'posts': posts
    }
    return render(request, 'index.html', context=d)


def about_view(request):
    return render(request, 'about.html')


def blog_view(request):
    data = request.GET
    category = data.get('category')
    page = request.GET.get('page', 1)
    if category:
        posts = Post.objects.filter(is_published=True, category_id=category)
    else:
        posts = Post.objects.filter(is_published=True)
    post_obj = Paginator(posts, 1)
    d = {
        'posts': post_obj.page(page),
        'blog': 'active',
    }
    return render(request, 'blog.html', context=d)


def blog_detail_view(request, pk):
    post = Post.objects.filter(id=pk, is_published=True).first()
    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(post_id=pk, name=data.get('name'), email=data.get('email'),
                                     message=data.get('message'))
        obj.save()
        return redirect(f'/blog/{pk}')
    comments = Comment.objects.filter(post_id=pk)
    d = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog-single.html', context=d)
