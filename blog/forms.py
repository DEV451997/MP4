from django import forms
from .models import Author, Category, Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'

    thumbnail = forms.ImageField(label='Thumbnail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categories = Category.objects.all()
        self.posts = Post.objects.all() 