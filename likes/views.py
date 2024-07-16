from rest_framework import generics, permissions
from .models import PostLike
from .serializers import PostLikeSerializer
from memovault_api.permissions import IsOwnerOrReadOnly

class PostLikeList(generics.ListCreateAPIView):

    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostLike.objects.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class PostLikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()