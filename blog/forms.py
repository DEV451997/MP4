from django import forms
from .models import Author, Category, Post

class PostForm(forms.ModelForm):

    SLUG_CHOICES = [
        ('Mt-Olympus-Events', 'Mt-Olympus-Events'),
        ('Mt-Olympus-Clothing', 'Mt-Olympus-Clothing'),
        ('Mt-Olympus-Supplements', 'Mt-Olympus-Supplements'),
    ]

    slug = forms.ChoiceField(choices=SLUG_CHOICES, label='Slug')
    
    class Meta:
        model = Post
        fields = '__all__'

    thumbnail = forms.ImageField(label='Thumbnail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categories = Category.objects.all()
        self.posts = Post.objects.all() 