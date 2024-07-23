from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from memovault_api.permissions import IsOwnerOrReadOnly

class FollowerList(generics.ListCreateAPIView):
    """
    List all followers or create a new follower relationship.

    This view provides two functionalities:
    - List all followers for both authenticated and unauthenticated users.
    - Allows authenticated users to create a new follower relationship.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use for the view.
        permission_classes (list): Specifies the permissions required to access the view.

    Methods:
        get_queryset: Returns the queryset of all followers.
        perform_create: Associates the created follower relationship with the authenticated user as the owner.
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a specific follower relationship.

    This view provides two functionalities:
    - Retrieve the details of a specific follower relationship.
    - Delete a specific follower relationship.

    Attributes:
        queryset (QuerySet): Specifies the queryset to use for retrieving the follower relationships.
        serializer_class (Serializer): Specifies the serializer to use for the view, which is `FollowerSerializer`.
        permission_classes (list): Specifies the permissions required to access the view. Uses `IsOwnerOrReadOnly`.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer