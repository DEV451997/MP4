from django.contrib import admin
from .models import Author, Category, Post

# Registering models with the Django admin site

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
