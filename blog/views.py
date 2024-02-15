from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib import messages

def blog(request):
    posts = Post.objects.order_by('-featured',)
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/blog.html', context)


@login_required
def blog_post(request):
    """ Add a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect('blog')
        else:
            messages.error(request, 'Failed to add blog post. Please ensure the form is valid.')
    else:
        form = PostForm()
        
    template = 'blog/blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, post_id):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Blog!')
            return redirect('blog')  
        else:
            messages.error(request, 'Failed to update blog post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')
    

    template = 'blog/edit_blog.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete a blog post  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Blog Post deleted!')
    return redirect('blog')