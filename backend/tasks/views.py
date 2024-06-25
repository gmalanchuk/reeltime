from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tasks.models import Board, Column, Task
from tasks.permissions import IsOwnerOrBoardAdminPermission, CanDragTasksPermission, CanCreateTaskPermission
from tasks.serializers import BoardSerializer, ColumnSerializer, TaskSerializer, TaskColumnFieldUpdateSerializer, \
    TaskExecutorFieldUpdateSerializer


@extend_schema(tags=['Boards'])
class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_permissions(self):  # TODO: DRY
        if self.action == 'create':
            return (IsAuthenticated(),)
        elif self.action == 'destroy':
            return (IsOwnerOrBoardAdminPermission(),)
        # elif self.action in ('update', 'partial_update'):
        #     return (IsCanUpdateBoard(),)

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
            return (CanCreateTaskPermission(),)
        elif self.action in ('update', 'partial_update'):
            return (CanDragTasksPermission(),)
        # elif self.action == 'destroy':
            # return (CanDeleteTaskPermission(),

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            user = self.request.user
            board = self.get_object().column.board

            if user.is_superuser or board.owner == user or self.get_object().owner == user:
                return TaskSerializer
            elif board.board_users.get(user=user).role.can_change_executor:
                return TaskExecutorFieldUpdateSerializer
            else:
                return TaskColumnFieldUpdateSerializer

        return super().get_serializer_class()
