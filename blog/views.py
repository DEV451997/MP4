from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from .forms import PostForm

def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/blog.html', context)


@login_required
def edit_blog(request, post_id):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administrators can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Blog!')
            return redirect(reverse('blog', args=[post.id]))  
        else:
            messages.error(request, 'Failed to update blog post. Please ensure the form is valid.')
    

    template = 'blog/edit_blog.html'
    context = {
        'post': post,
        'form': PostForm,
    }

    return render(request, template, context)