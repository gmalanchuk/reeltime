from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tasks.models import Board, Column, Task
from tasks.permissions import IsOwnerOrAdminPermission, CanDragTasksPermission
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
            return (IsOwnerOrAdminPermission(),)
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
            # написать кастомный пермишен, который проверяет, что пользователь состоит в board_users и что у него есть право на создание задачи
            return (IsAuthenticated(),)
        elif self.action in ('update', 'partial_update'):
            return (CanDragTasksPermission(),)

        return super().get_permissions()

    def get_serializer_class(self):
        user = self.request.user
        board = self.get_object().column.board

        if self.action in ('update', 'partial_update'):
            if user.is_superuser or board.owner == user:
                return TaskSerializer
            elif board.board_users.get(user=user).role.can_change_executor:
                return TaskExecutorFieldUpdateSerializer
            # elif todo если у пользователя есть определенное право, то он тоже может обновлять все поля
            else:
                return TaskColumnFieldUpdateSerializer

        return super().get_serializer_class()
