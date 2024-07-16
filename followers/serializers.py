from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate(self, data):
        if 'owner' not in data:
            data['owner'] = self.context['request'].user

        if data['owner'] == data['followed']:
            raise serializers.ValidationError({'details': "A user cannot follow themselves."})
        return data

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })