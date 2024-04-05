from rest_framework import serializers
from server.models import Category, Server, Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["id", "name", "owner", "topic", "server", "is_active", "created_time", "updated_time"]


class ServerSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    # channel_detail = ChannelSerializer(many=True)

    class Meta:
        model = Server
        fields = ["id", "name", "category", "description", "is_active", "member_count",
                  "created_time", "updated_time"]

    def get_member_count(self, obj):
        if hasattr(obj, "member_count"):
            return obj.member_count
        else:
            return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        member_count = self.context.get("member_count")
        if not member_count:
            data.pop("member_count")
        return data
