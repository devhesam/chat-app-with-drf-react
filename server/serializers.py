from rest_framework import serializers
from server.models import Category, Server


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ["id", "name", "category", "description", "member", "is_active"]
