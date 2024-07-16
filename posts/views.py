from rest_framework import generics, permissions
from memovault_api.permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from .models import Post



class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()