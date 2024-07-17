from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Report
        fields = ['id', 'owner', 'post', 'post_title', 'reason', 'custom_reason', 'created_at', 'updated_at']

    def validate(self, data):
        if data['reason'] == 'other' and not data.get('custom_reason'):
            raise serializers.ValidationError("A reason is required when 'Other' is selected.")
        return data

    def create(self, validated_data):
        return Report.objects.create(**validated_data)
