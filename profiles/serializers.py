from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    follows_you = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

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
            'name', 'hobbies', 'bio', 'image', 'follows_you'
        ]