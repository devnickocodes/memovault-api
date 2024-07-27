from rest_framework import serializers
from django.db import IntegrityError
from .models import PostLike, CommentLike


class PostLikeSerializer(serializers.ModelSerializer):
    """
    Serializer which handles the representation and validation of
                                             `PostLike` instances.

    Attributes:
        owner (ReadOnlyField): The username of the user who liked the post.
        post (ForeignKey): The post that was liked.
        created_at (DateTimeField): The timestamp when the like was created.

    Methods:
        create(validated_data): Handles the creation of a new `PostLike`
                                instance, and raises a validation error if a
                                duplicate entry is detected.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PostLike
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        """
        Handles the creation of a new `PostLike`
        instance, and raises a validation error if a
        duplicate entry is detected.
        """
        try:
            return super().create(validated_data)
        except IntegrityError as exc:
            raise serializers.ValidationError(
                {'detail': 'possible duplicate'}
            ) from exc


class CommentLikeSerializer(serializers.ModelSerializer):
    """
    Serializer which handles the representation and validation of `CommentLike`
                                                                     instances.

    Attributes:
        owner (ReadOnlyField): The username of the user who liked the comment.
        comment (ForeignKey): The comment that was liked.
        created_at (DateTimeField): The timestamp when the like was created.

    Methods:
        create(validated_data): Handles the creation of a new `CommentLike`
                                instance, and raises a validation error if a
                                duplicate entry is detected.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CommentLike
        fields = ['id', 'created_at', 'owner', 'comment']

    def create(self, validated_data):
        """
        Handles the creation of a new `CommentLike`
        instance, and raises a validation error if a
        duplicate entry is detected.
        """
        try:
            return super().create(validated_data)
        except IntegrityError as exc:
            raise serializers.ValidationError(
                {'detail': 'possible duplicate'}
            ) from exc
