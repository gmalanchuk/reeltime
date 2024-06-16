from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from tasks.models import Board
from tasks.serializers import BoardSerializer


@extend_schema(tags=['Boards'])
class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
