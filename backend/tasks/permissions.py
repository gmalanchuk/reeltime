from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from tasks.models import Board, Column


class IsOwnerOrBoardAdminPermission(BasePermission):
    def has_permission(self, request, view, board: Board = None):
        # if user is an admin - return True
        if request.user.is_superuser:
            return True

        # if board is not passed as an argument - get it from the view (because this permission is used in BoardViewSet)
        if not board:
            board_id = view.kwargs['pk']
            board = Board.objects.get(pk=board_id)

        # if user is a board owner - return True
        if board.owner == request.user:
            return True

        return False


# todo написать один общий пермишен для проверки всех прав
class CanDragTasksPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        board = view.get_object().column.board

        # if user is an admin or board owner - return True
        if IsOwnerOrBoardAdminPermission().has_permission(request, view, board=board):
            return True

        # if user is a board member and has the right to drag tasks - return True
        if board.board_users.filter(user=user).exists():
            if board.board_users.get(user=user).role.can_drag_tasks:
                return True

        return False


class CanCreateTaskPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        board = get_object_or_404(Column, pk=request.data['column']).board

        # if user is an admin or board owner - return True
        if IsOwnerOrBoardAdminPermission().has_permission(request, view, board=board):
            return True

        # if user is a board member and has the right to create tasks - return True
        if board.board_users.filter(user=user).exists():
            if board.board_users.get(user=user).role.can_create_tasks:
                return True

        return False


class CanDeleteTaskPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        board = view.get_object().column.board

        # if user is an admin or board owner - return True
        if IsOwnerOrBoardAdminPermission().has_permission(request, view, board=board):
            return True

        # if user is a board member and has the right to manage all tasks - return True
        if board.board_users.filter(user=user).exists():
            if board.board_users.get(user=user).role.can_manage_all_tasks:
                return True
            elif view.get_object().owner == user:  # if user is a task owner - return True
                return True

        return False
