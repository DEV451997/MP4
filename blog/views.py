from django.shortcuts import render
from .models import Post, Category

def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/blog.html', context)
