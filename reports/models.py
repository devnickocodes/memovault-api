from django.db import models
from django.contrib.auth.models import User
from posts.models import Post  

class Report(models.Model):
    """
     Stores a single report entry.

    Attributes:
        owner (ForeignKey): The user who created the report. Related to :model:`auth.User`.
        post (ForeignKey): The post that is being reported. Related to :model:`posts.Post`.
        reason (CharField): The reason for the report, chosen from predefined options.
        custom_reason (TextField): An optional custom reason provided by the user if the predefined options are not sufficient.
        created_at (DateTimeField): The timestamp when the report was created.
        updated_at (DateTimeField): The timestamp when the report was last updated.

    Methods:
        __str__: Returns a string representation of the report including the owner, post, and reason.

    Meta:
        ordering (list): Orders reports by the `created_at` field in descending order.
    """
    REPORT_REASONS = [
        ('spam', 'Spam'),
        ('inappropriate', 'Inappropriate Content'),
        ('harassment', 'Harassment'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_reports')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_reports')
    reason = models.CharField(max_length=100, choices=REPORT_REASONS)
    custom_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner} reported {self.post} for {self.reason}"


