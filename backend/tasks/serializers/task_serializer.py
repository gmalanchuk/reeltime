from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ("id", "description", "column", "owner", "executor", "created_at", "updated_at")


class TaskColumnFieldUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating the COLUMN field in the Task model"""

    class Meta:
        model = Task
        fields = ("column",)


class TaskExecutorFieldUpdateSerializer(TaskColumnFieldUpdateSerializer):
    """Serializer for updating the EXECUTOR or/and COLUMN field in the Task model"""

    class Meta:
        model = Task
        fields = TaskColumnFieldUpdateSerializer.Meta.fields + ("executor",)
