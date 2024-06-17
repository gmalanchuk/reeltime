from rest_framework import serializers

from tasks.models import Board, Column


class BoardSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Board
        fields = ("id", "name", "description", "user", "created_at", "updated_at")


class ColumnSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Column
        fields = ("id", "name", "board", "user", "created_at", "updated_at")
