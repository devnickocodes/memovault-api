from django.db.models import Count
from rest_framework import generics, permissions, filters
from memovault_api.permissions import IsOwnerOrReadOnly, IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):

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
    permission_classes = [IsOwnerOrReadOnly | IsAdmin]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        comment_likes_count=Count('likes')
    ).order_by('created_at')
