from django.db.models import Count
from rest_framework import generics, permissions, filters
from memovault_api.permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from .models import Post



class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count = Count('comment'),
        post_likes_count = Count('likes')
    ).order_by('created_at')
    filter_backends = [
            filters.OrderingFilter
        ]
    ordering_fields  = [
        'comments_count',
        'post_likes_count',
        'likes__created_at'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count = Count('comment'),
        post_likes_count = Count('likes')
    ).order_by('created_at')








