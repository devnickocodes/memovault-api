from django.db.models import Count
from rest_framework import generics, permissions, filters
from memovault_api.permissions import IsOwnerOrReadOnly, IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List all comments or create a new comment.

    This view handles listing all comments with the ability to filter and order the results.
    It provides functionalities to filter comments by post and to sort the comments
    based on the number of likes.

    Attributes:
        serializer_class (Serializer): The serializer class used to validate and serialize comment data.
        permission_classes (list): A list of permission classes to enforce access control. 
        Allows authenticated users to create comments and read-only access for unauthenticated users.
        queryset (QuerySet): The queryset of `Comment` instances with an annotation for comment likes count and ordered by creation date.
        filter_backends (list): List of filter backends to apply for filtering and ordering.
        filterset_fields (list): Fields that can be filtered using DjangoFilterBackend.
        ordering_fields (list): Fields that can be used for ordering the results.

    Methods:
        perform_create: Saves the comment with the current user set as the owner when a new comment is created.
    """
    serializer_class = CommentSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    queryset = Comment.objects.annotate(
        comment_likes_count=Count('likes')
    ).order_by('created_at')
    serializer_class = CommentSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]

    filterset_fields = [
        'post'
    ]

    ordering_fields = [
        'comment_likes_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific comment.

    This view provides functionalities to retrieve the details of a single comment,
    update an existing comment, or delete a comment. It includes permissions to ensure
    that only the owner or an admin can modify or delete a comment.

    Attributes:
        serializer_class (Serializer): The serializer class used to validate and serialize comment data.
        permission_classes (list): A list of permission classes to enforce access control. 
        Allows only the owner or the admin to update or delete the comment.
        queryset (QuerySet): The queryset of `Comment` instances with an annotation for comment likes count, ordered by creation date.
    """
    permission_classes = [IsOwnerOrReadOnly | IsAdmin]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        comment_likes_count=Count('likes')
    ).order_by('created_at')
