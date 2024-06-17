from rest_framework import serializers

from tasks.models import Board, Column, Task


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Board
        fields = ("id", "name", "description", "owner", "created_at", "updated_at")


class ColumnSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Column
        fields = ("id", "name", "board", "owner", "created_at", "updated_at")


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ("id", "description", "column", "owner", "executor", "created_at", "updated_at")
