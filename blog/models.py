from django.contrib.auth import get_user_model
from django.db import models

# Getting the User model dynamically
User = get_user_model()


class Author(models.Model):
    """
    Model representing an author with a,
    one-to-one relationship to the User model.

    Attributes:
        user (User): One-to-one field representing the associated user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the author.

        Returns:
            str: Username of the associated user.
        """
        return self.user.username


class Category(models.Model):
    """
    Model representing a blog category.

    Attributes:
        title (str): The title of the category.
        subtitle (str): The subtitle of the category.
        slug (str): The slug of the category.
        thumbnail (ImageField):
        The thumbnail image associated with the category.
    """

    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        """
        Return a string representation of the category.

        Returns:
            str: The title of the category.
        """
        return self.title


class Post(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (str): The title of the post.
        slug (str): The slug of the post.
        overview (str): The overview text of the post.
        timestamp (DateTimeField): The timestamp when the post was created.
        content (str): The content of the post.
        author (Author): The author of the post.
        thumbnail (ImageField): The thumbnail image associated with the post.
        categories (ManyToManyField): The categories associated with the post.
        featured (bool): Indicates whether the post is featured.
    """

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        """
        Return a string representation of the post.

        Returns:
            str: The title of the post.
        """
        return self.title
