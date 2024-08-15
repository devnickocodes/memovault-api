from rest_framework import serializers
from posts.models import Post
from likes.models import PostLike


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer which handles the representation and validation of `Post`
                                                              instances.

    Attributes:
        owner (ReadOnlyField): The username of the user who created the post.
        is_owner (SerializerMethodField): Boolean indicating if the requesting
                                                 user is the owner of the post.
        is_admin (SerializerMethodField): Boolean indicating if the requesting
                                                              user is an admin.
        profile_id (ReadOnlyField): The ID of the profile associated with
                                                           the post owner.
        profile_image (ReadOnlyField): The URL of the profile image of the
                                                                post owner.
        post_like_id (SerializerMethodField): The ID of the post like
                                     associated with the request user.
        comments_count (ReadOnlyField): The number of comments associated
                                                            with the post.
        post_likes_count (ReadOnlyField): The number of likes associated with
                                                                     the post.

    Methods:
        get_is_owner: Returns True if the requesting user is the owner of the
                                                                         post.
        get_post_like_id: Returns the ID of the post like by the requesting
                                                         user, if it exists.
        get_is_admin: Returns True if the requesting user is an admin.
        validate_image: Validates the image file to ensure it meets specific
                                                 size and dimension criteria.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    post_like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    post_likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Determines if the requesting user is the owner of the post.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_post_like_id(self, obj):
        """
        Retrieves the ID of the post like by the requesting user, if exists.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            post_like_id = PostLike.objects.filter(
                owner=user, post=obj
            ).first()
            return post_like_id.id if post_like_id else None
        return None

    def get_is_admin(self):
        """
        Determines if the requesting user is an admin.
        """
        request = self.context['request']
        return request.user.is_staff

    def validate_image(self, value):
        """
        Validates the image file for size and dimensions.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'is_admin', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'post_like_id',
            'comments_count', 'post_likes_count'
        ]
