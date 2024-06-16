from rest_framework.viewsets import ModelViewSet

from tasks.models import Board
from tasks.serializers import BoardSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
