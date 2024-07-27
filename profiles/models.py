from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile associated with :model:`auth.User`.

    Attributes:
        owner (ForeignKey): The owner of the profile.
        created_at (DateTimeField): The timestamp when the profile was created.
        updated_at (DateTimeField): The timestamp when the profile was
                                                          last updated.
        name (CharField): The name of the user (optional).
        hobbies (CharField): The hobbies of the user (optional).
        bio (TextField): A short biography of the user (optional).
        image (ImageField): Profile image of the user (optional).

    Methods:
        create_profile: Signal handler function that creates a profile
                                            when a new user is created.

    Meta:
        ordering (list): Orders profiles by the `created_at`
                                  field in descending order.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    hobbies = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../profile_image_placeholder_rfrtkm'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s Profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler function to automatically create a `Profile` instance
    whenever a new `User` instance is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
