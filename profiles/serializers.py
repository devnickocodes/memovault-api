from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer which handles the representation and validation of `Profile` instances.

    Attributes:
        owner (ReadOnlyField): The username of the user to whom the profile belongs.
        is_owner (SerializerMethodField): A boolean indicating if the requesting user is the owner of the profile.
        follows_you (SerializerMethodField): A boolean indicating if the owner of the profile is following the requesting user.
        following_id (SerializerMethodField): The ID of the follow relationship if the requesting user is following the profile's owner.
        posts_count (ReadOnlyField): The number of posts made by the profile's owner.
        followers_count (ReadOnlyField): The number of followers the profile's owner has.
        following_count (ReadOnlyField): The number of users the profile's owner is following.

    Methods:
        get_is_owner: Determines if the requesting user is the owner of the profile.
        get_following_id: Retrieves the ID of the follow relationship if the requesting user is following the profile's owner.
        get_follows_you: Checks if the owner of the profile is following the requesting user.
        validate_image: Validates the profile image to ensure it adheres to size and dimension restrictions.

    Meta:
        fields (list): A list of fields to include in the serialized output.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    follows_you = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    def validate_image(self, value):
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

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    def get_follows_you(self, obj):
        request_user = self.context['request'].user
        if request_user.is_authenticated:
            following = Follower.objects.filter(
                owner=obj.owner,
                followed=request_user
            ).exists()
            return following
        return False

    class Meta:
        model = Profile
        fields = [
            'id', 'owner','is_owner', 'created_at', 'updated_at',
            'name', 'hobbies', 'bio', 'image', 'follows_you', 'following_id',
            'posts_count', 'followers_count', 'following_count'
        ]