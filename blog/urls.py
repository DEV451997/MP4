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

"""
URL patterns for blog-related views.

This list of URL patterns,
maps specific URL paths to corresponding view functions
defined in the 'views.py'
module of the 'blog' app.Each path consists of a unique
identifier and
specifies,the view function that should be invoked when the URL is
accessed. The 'name' attribute
is used to uniquely identify each URL pattern and
can be referred to in Django templates or views to generate URLs dynamically.
"""
