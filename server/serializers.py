from rest_framework import serializers
from server.models import Category, Server, Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["id", "name", "owner", "topic", "server", "is_active", "created_time", "updated_time"]


class ServerSerializer(serializers.ModelSerializer):
    channel_detail = ChannelSerializer(many=True)

    class Meta:
        model = Server
        fields = ["id", "name", "category", "description", "member", "is_active", "created_time", "updated_time"]
