from rest_framework import serializers

from tasks.models import Column


class ColumnSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Column
        fields = ("id", "name", "board", "owner", "created_at", "updated_at")
