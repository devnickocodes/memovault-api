from django.db import models
from django.contrib.auth.models import User
from posts.models import Post  

class Report(models.Model):

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