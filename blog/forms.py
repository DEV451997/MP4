from django import forms
from .models import Author, Category, Post


class PostForm(forms.ModelForm):
    """
    Django form for the Post model.

    This form allows users to create or update a post. It includes fields
    such as 'title', 'content', 'author',
    'categories', 'slug', and 'thumbnail'.

    Attributes:
        SLUG_CHOICES (list):
        List of tuples representing choices for the 'slug' field.
    """

    SLUG_CHOICES = [
        ('Mt-Olympus-Events', 'Mt-Olympus-Events'),
        ('Mt-Olympus-Clothing', 'Mt-Olympus-Clothing'),
        ('Mt-Olympus-Supplements', 'Mt-Olympus-Supplements'),
    ]

    slug = forms.ChoiceField(choices=SLUG_CHOICES, label='Slug')

    class Meta:
        """
        Meta class for the PostForm.

        Specifies metadata options for the form, such as the associated model
        and the fields to include.
        """
        model = Post
        fields = '__all__'  # Including fields from the Post model in the form

    thumbnail = forms.ImageField(label='Thumbnail')

    def __init__(self, *args, **kwargs):
        """
        Initialize the PostForm instance.

        Retrieves all categories and posts from the database and stores them
        as instance attributes.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.categories = Category.objects.all()
        self.posts = Post.objects.all()
