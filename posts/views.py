from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from memovault_api.permissions import IsOwnerOrReadOnly, IsAdmin
from .serializers import PostSerializer
from .models import Post



class PostList(generics.ListCreateAPIView):
    """
    List all posts or create a new post.

    This view provides two functionalities:
    - List all posts for authenticated users, with the ability to filter, search, and order the results.
    - Allows authenticated users to create a new post.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use for the view.
        permission_classes (list): Specifies the permissions required to access the view.
        queryset (QuerySet): The queryset used to retrieve posts, annotated with comment and like counts, and ordered by creation date.
        filter_backends (list): Specifies the filter backends used for filtering, searching, and ordering posts.
        filterset_fields (list): The fields used for filtering posts.
        ordering_fields (list): The fields that can be used for ordering posts.
        search_fields (list): The fields used for searching posts.

    Methods:
        perform_create: Associates the created post with the authenticated user as the owner.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count = Count('comment'),
        post_likes_count = Count('likes')
    ).order_by('created_at')
    filter_backends = [
            filters.OrderingFilter,
            filters.SearchFilter,
            DjangoFilterBackend,
        ]
    
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile'
    ]

    ordering_fields  = [
        'comments_count',
        'post_likes_count',
        'likes__created_at'
    ]

    search_fields = [
        'owner__username',
        'title'
    ]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific post.

    This view provides three functionalities:
    - Retrieve the details of a specific post.
    - Update the details of a specific post if the requesting user is the owner or an admin.
    - Delete a specific post if the requesting user is the owner or an admin.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use for the view.
        permission_classes (list): Specifies the permissions required to access the view.
        queryset (QuerySet): The queryset used to retrieve posts, annotated with comment and like counts, and ordered by creation date.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly | IsAdmin]
    queryset = Post.objects.annotate(
        comments_count = Count('comment'),
        post_likes_count = Count('likes')
    ).order_by('created_at')








