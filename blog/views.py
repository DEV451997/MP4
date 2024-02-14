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

def edit_blog(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:blog', post_id=post.id)  # Redirect to detail view
    else:
        form = BlogPostForm(instance=post)
    
    return render(request, 'edit_blog.html', {'form': form})