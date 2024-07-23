from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Represents a single post related to :model:`auth.User`.

    Attributes:
        owner (:model:`auth.User`): The user who created the post.
        created_at (DateTimeField): The timestamp when the post was created.
        updated_at (DateTimeField): The timestamp when the post was last updated.
        title (CharField): The title of the post.
        content (TextField): The content of the post.
        image (ImageField): An optional image associated with the post.
    
    Meta:
        ordering (list): Orders records by the `created_at` field in descending order.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='images/', default='../post_placeholder_image_et5qsq', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'