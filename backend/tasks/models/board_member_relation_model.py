from django.db import models

from tasks.models import AbsTimeStampModel


class BoardMemberRelation(AbsTimeStampModel):
    user = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="board_users")
    board = models.ForeignKey(to="Board", on_delete=models.CASCADE, related_name="board_users")
    role = models.ForeignKey(to="Role", on_delete=models.CASCADE, related_name="board_users")

    class Meta:
        unique_together = ('user', 'board')

    def __str__(self):
        return f"ID: {self.pk} | User: {self.user} | Board ID: {self.board.pk} | Role Name: {self.role.name}"
