from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer which handles the representation and validation of follow relationships between users.
    It provides functionality to ensure that a user cannot follow themselves and manages potential
    duplicate entries.

    Attributes:
        owner (ReadOnlyField): The username of the user who is following another user. 
        followed (PrimaryKeyRelatedField): The user who is being followed. The field will represent
        the ID of the user being followed.
        created_at (ReadOnlyField): The timestamp when the follow relationship was created.

    Methods:
        validate: Ensures that a user cannot follow themselves and assigns the current request user
            as the `owner` if not already provided.
        create: Handles creation of a follow relationship and raises a validation error if a duplicate
            entry is detected.

    Meta:
        model (Model): The model class being serialized, which is `Follower`.
        fields (list): The fields to be included in the serialized representation. 
    """
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed', 'created_at']

    def validate(self, data):
        if 'owner' not in data:
            data['owner'] = self.context['request'].user

        if data['owner'] == data['followed']:
            raise serializers.ValidationError({'details': "A user cannot follow themselves."})
        return data


    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
