from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tasks.models import Board, Column, Task
from tasks.permissions import IsOwnerOrAdmin, IsCanUpdateBoard
from tasks.serializers import BoardSerializer, ColumnSerializer, TaskSerializer


@extend_schema(tags=['Boards'])
class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_permissions(self):  # TODO: DRY
        if self.action == 'create':
            return (IsAuthenticated(),)
        elif self.action == 'destroy':
            return (IsOwnerOrAdmin(),)
        elif self.action in ('update', 'partial_update'):
            return (IsCanUpdateBoard(),)

        return super().get_permissions()


@extend_schema(tags=['Columns'])
class ColumnViewSet(ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def get_permissions(self):  # TODO: DRY
        if self.action == 'create':
            return (IsAuthenticated(),)
        return super().get_permissions()


@extend_schema(tags=['Tasks'])
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):  # TODO: DRY
        if self.action == 'create':
            return (IsAuthenticated(),)
        return super().get_permissions()
