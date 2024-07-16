from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from memovault_api.permissions import IsOwnerOrReadOnly

class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Follower.objects.filter(owner=self.request.user)
        else:
            return Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)