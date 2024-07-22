from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count = Count('comment'),
        post_likes_count = Count('likes')
    ).order_by('created_at')








