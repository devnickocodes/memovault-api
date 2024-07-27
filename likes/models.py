from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment


class PostLike(models.Model):
    """
    Stores a single like entry related to :model:`auth.User`.
    And :model:`posts.Post`.

    Attributes:
        owner (ForeignKey): The user who liked the post.
        post (ForeignKey): The post that was liked.
        created_at (DateTimeField): The timestamp when the like was created.

    Meta:
        ordering (list): Orders records by the `created_at` field
                                              in descending order.
        unique_together (list): Ensures that each combination of
                                    `owner` and `post` is unique.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f"{self.owner} likes {self.post}"


class CommentLike(models.Model):
    """
    Stores a single like entry related to :model:`auth.User`.
    And :model:`comments.Comment`.

    Attributes:
        owner (ForeignKey): The user who liked the comment.
        comment (ForeignKey): The comment that was liked.
        created_at (DateTimeField): The timestamp when the like was created.

    Meta:
        ordering (list): Orders records by the `created_at`
                                  field in descending order.
        unique_together (list): Ensures that each combination of
                                 `owner` and `comment` is unique.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
                                related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'comment']

    def __str__(self):
        return f"{self.owner} likes {self.comment}"
