from rest_framework import generics, permissions
from .models import PostLike
from .serializers import PostLikeSerializer

class PostLike(generics.ListCreateAPIView):

    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostLike.objects.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)