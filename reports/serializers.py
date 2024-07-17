from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Report
        fields = ['id', 'owner', 'post', 'post_title', 'reason', 'custom_reason', 'created_at', 'updated_at']

    def create(self, validated_data):
            return Report.objects.create(**validated_data)