from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProfileSerializer
from .models import Profile
from memovault_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles or filter/search through existing profiles.

    This view provides two functionalities:
    - List all profiles for authenticated users, with the ability to filter, search, and order the results.
    - Allows querying of profiles based on owner, hobbies as well as posts, followers and following

    Attributes:
        serializer_class (ProfileSerializer): Specifies the serializer to use for the view.
        queryset (QuerySet): The queryset used to retrieve profiles, annotated with counts of posts, followers, and following, and ordered by creation date.
        filter_backends (list): Specifies the filter backends used for filtering, searching, and ordering profiles.
        filterset_fields (list): The fields used for filtering profiles.
        search_fields (list): The fields used for searching profiles.
        ordering_fields (list): The fields that can be used for ordering profiles.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile'
    ]

    search_fields = [
        'owner__username',
        'hobbies',
    ]

    ordering_fields  = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a specific profile.

    This view provides two functionalities:
    - Retrieve detailed information about a specific profile.
    - Allows updating of the profile if the authenticated user has the appropriate permissions.

    Attributes:
        permission_classes (list): Specifies the permissions required to update the profile.
        queryset (QuerySet): The queryset used to retrieve and annotate a profile with counts of posts, followers, and following.
        serializer_class (ProfileSerializer): Specifies the serializer to use for the view.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer