from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class Follower(models.Model):
    """
    Stores a follow relationship between two users
    related to :model:`auth.User`.

    Attributes:
        owner (ForeignKey): The user who is following another user.
                                     Related to :model:`auth.User`.
        followed (ForeignKey): The user who is being followed.
                                 Related to :model:`auth.User`.
        created_at (DateTimeField): The timestamp when the follow
                                         relationship was created.

    Methods:
        clean: Ensures that a user cannot follow themselves.

    Meta:
        ordering (list): Orders records by the `created_at`
                                 field in descending order.
        unique_together (list): Ensures that each combination of `owner`
                                               and `followed` is unique.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='followed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def clean(self):
        if self.owner == self.followed:
            raise ValidationError("A user cannot follow themselves.")

    def __str__(self):

        return f"{self.owner} {self.followed}"
