from rest_framework import serializers

from tasks.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ("id", "name", "description", "created_at", "updated_at")
