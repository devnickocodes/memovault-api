from rest_framework import serializers
from posts.models import Post
from likes.models import PostLike

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    post_like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    post_likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    def get_post_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            post_like_id = PostLike.objects.filter(
                owner=user, post=obj
            ).first()
            return post_like_id.id if post_like_id else None
        return None


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

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'post_like_id',
            'comments_count', 'post_likes_count'
        ]