from django import forms
from .models import Author, Category, Post

# Django form for the Post model


class PostForm(forms.ModelForm):

    SLUG_CHOICES = [
        ('Mt-Olympus-Events', 'Mt-Olympus-Events'),
        ('Mt-Olympus-Clothing', 'Mt-Olympus-Clothing'),
        ('Mt-Olympus-Supplements', 'Mt-Olympus-Supplements'),
    ]

    slug = forms.ChoiceField(choices=SLUG_CHOICES, label='Slug')

    class Meta:
        model = Post
        fields = '__all__'  # Including fields from the Post model in the form

    thumbnail = forms.ImageField(label='Thumbnail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categories = Category.objects.all()
        self.posts = Post.objects.all()
