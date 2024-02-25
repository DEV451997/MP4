from django.urls import path
from .views import blog
from . import views

# Django urlpatterns for blog-related views
urlpatterns = [
    path('', blog, name='blog'),
    path('add/', views.blog_post, name='blog_post'),
    path('edit/<int:post_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
