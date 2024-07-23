from rest_framework import generics, permissions
from .models import PostLike, CommentLike
from .serializers import PostLikeSerializer, CommentLikeSerializer
from memovault_api.permissions import IsOwnerOrReadOnly

class PostLikeList(generics.ListCreateAPIView):
    """
    List and create post likes.

    This view provides two functionalities:
    - List all `PostLike` instances.
    - Allows authenticated users to create a new `PostLike` instance.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use for the view, which is `PostLikeSerializer`.
        permission_classes (list): Specifies the permissions required to access the view. Uses `IsAuthenticatedOrReadOnly`.
        queryset (QuerySet): The queryset of `PostLike` instances to be used for the list view.

    Methods:
        perform_create(serializer): Associates the created `PostLike` with the authenticated user.
    """
    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostLike.objects.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class PostLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete a specific post like.

    This view provides:
    - Retrieve a single `PostLike` instance by its ID.
    - Delete a `PostLike` instance if the user has the required permissions.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use for the view, which is `PostLikeSerializer`.
        permission_classes (list): Specifies the permissions required to access the view. Uses `IsOwnerOrReadOnly`.
        queryset (QuerySet): The queryset of `PostLike` instances to be used for the detail view.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostLikeSerializer
    queryset = PostLike.objects.all()



class CommentLikeList(generics.ListCreateAPIView):
    """
    List and create comment likes.

    This view provides two functionalities:
    - List all `CommentLike` instances.
    - Allows authenticated users to create a new `CommentLike` instance.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use for the view, which is `CommentLikeSerializer`.
        permission_classes (list): Specifies the permissions required to access the view. Uses `IsAuthenticated`.
        queryset (QuerySet): The queryset of `CommentLike` instances to be used for the list view.

    Methods:
        perform_create(serializer): Associates the created `CommentLike` with the authenticated user.
    """
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete a specific comment like.

    This view provides:
    - Retrieve a single `CommentLike` instance by its ID.
    - Delete a `CommentLike` instance if the user has the required permissions.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use for the view, which is `CommentLikeSerializer`.
        permission_classes (list): Specifies the permissions required to access the view. Uses `IsOwnerOrReadOnly`.
        queryset (QuerySet): The queryset of `CommentLike` instances to be used for the detail view.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()