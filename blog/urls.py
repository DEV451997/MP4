from django.urls import path
from .views import blog
from . import views

urlpatterns = [
    path('', blog, name='blog'),
    path('edit/<int:post_id>/', views.edit_blog, name='edit_blog'),
]
