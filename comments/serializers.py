from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from likes.models import CommentLike
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer used to convert `Comment` instances to JSON format and
    validate data when creating or updating comments.

    Attributes:
        owner (ReadOnlyField): The username of the user who is
                                      the owner of the comment.
        is_owner (SerializerMethodField): Indicates whether the request
                                       user is the owner of the comment.
        profile_id (ReadOnlyField): The ID of the profile associated with
                                                      the comment's owner.
        profile_image (ReadOnlyField): The URL of the profile image
                                             of the comment's owner.
        created_at (SerializerMethodField): The timestamp when
                                       the comment was created.
        updated_at (SerializerMethodField): The timestamp when the
                                          comment was last updated.
        comment_like_id (SerializerMethodField): The ID of the comment like
                                           associated with the request user.
        comment_likes_count (ReadOnlyField): The number of likes associated
                                                           with the comment.

    Methods:
        get_is_owner: Returns a boolean indicating whether the
                      request user is the owner of the comment.
        get_is_admin: Returns a boolean indicating whether the
                                      request user is an admin.
        get_comment_like_id: Returns the ID of the comment like if the
                                    request user has liked the comment.
        get_created_at: Returns the creation timestamp of the comment.
        get_updated_at: Returns the last update timestamp of the comment.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    comment_like_id = serializers.SerializerMethodField()
    comment_likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Returns a boolean indicating whether the
        request user is the owner of the comment.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_is_admin(self):
        """
        Returns a boolean indicating whether the request user is an admin.
        """
        request = self.context['request']
        return request.user.is_staff

    def get_comment_like_id(self, obj):
        """
        Returns the ID of the comment like if
        the request user has liked the comment.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            comment_like_id = CommentLike.objects.filter(
                owner=user, comment=obj
            ).first()
            return comment_like_id.id if comment_like_id else None
        return None

    def get_created_at(self, obj):
        """
        Returns the creation timestamp of the
        comment in a human-readable format.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns the last update timestamp of the
        comment in a human-readable format.
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'is_admin', 'profile_id',
            'post', 'created_at', 'updated_at', 'content', 'profile_image',
            'comment_like_id', 'comment_likes_count'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Detailed serializer for the `Comment` model, extending `CommentSerializer`.

    Attributes:
        post (ReadOnlyField): The ID of the post associated with the comment.
    """
    post = serializers.ReadOnlyField(source='post.id')
