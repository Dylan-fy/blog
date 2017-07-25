from rest_framework import serializers
from .models import MessageBoard


class MessageBoardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    visitor_name = serializers.CharField(max_length=30)
    visitor_message = serializers.JSONField()
    message_create_at = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return MessageBoard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.visitor_name = validated_data.get(
            'visitor_name', instance.visitor_name)
        instance.visitor_message = validated_data.get(
            'visitor_message', instance.visitor_message)
        instance.message_create_at = validated_data.get(
            'message_create_at', instance.message_create_at)
        instance.save()
        return instance
