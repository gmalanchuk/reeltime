from rest_framework import serializers

from tasks.models import Board


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Board
        fields = ("id", "name", "description", "owner", "created_at", "updated_at")
