from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`.
    And :model:`posts.Post`.

    Attributes:
        owner (ForeignKey): The user who made the comment.
        post (ForeignKey): The post on which the comment was made.
        created_at (DateTimeField): The timestamp when the comment was created.
        updated_at (DateTimeField): The timestamp when the comment
                                                  was last updated.
        content (TextField): The content of the comment.
    Meta:
        ordering (list): Orders records by the `created_at` field
                                              in descending order.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s comment for: {self.post}"
