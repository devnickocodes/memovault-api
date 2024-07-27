from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer which handles the representation and validation of
                                               `Report` instances.

    Attributes:
        owner (ReadOnlyField): The username of the user who created the report.
        post_title (ReadOnlyField): The title of the post being reported.

    Methods:
        validate: Ensures that a custom reason is provided if 'Other' is
                                                  selected as the reason.
        create: Creates a new `Report` instance with the validated data.
        update: Updates an existing `Report` instance with the validated data.

    Meta:
        fields (list): The fields included in the serialized representation.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Report
        fields = ['id', 'owner', 'post', 'post_title', 'reason',
                  'custom_reason', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Ensures that a custom reason is provided if 'Other'
        is selected as the reason.
        """
        if data['reason'] == 'other' and not data.get('custom_reason'):
            raise serializers.ValidationError(
                "A reason is required when 'Other' is selected.")
        return data

    def create(self, validated_data):
        return Report.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.post = validated_data.get('post', instance.post)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.custom_reason = validated_data.get('custom_reason',
                                                    instance.custom_reason)
        instance.save()
        return instance
