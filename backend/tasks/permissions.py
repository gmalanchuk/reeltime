from rest_framework.permissions import BasePermission

from tasks.models import Board


class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        board_id = view.kwargs['pk']
        board = Board.objects.get(pk=board_id)
        if board.owner == request.user:
            return True

        return False


class IsCanUpdateBoard(BasePermission):  # todo переписать потом это в какую-то одну общую проверку(не только для права can_manage_board)
    """

    """


    # во первых надо будет брать какой-то непонятный объект из view.kwargs['pk'] и уже проверять его на принадлежность

    def has_permission(self, request, view):
        if not IsOwnerOrAdmin().has_permission(request, view):
            pass

        board_id = view.kwargs['pk']
        board = Board.objects.get(pk=board_id)

        if board.board_users.filter(user=request.user).exists():
            if board.board_users.get(user=request.user).role.can_manage_board:
                return True

        return False
