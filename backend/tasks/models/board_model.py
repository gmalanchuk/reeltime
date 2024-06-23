from django.db import models

from tasks.models import AbsTimeStampModel


class Board(AbsTimeStampModel):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, null=True, blank=True)
    # status = CharField
    owner = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="boards")
    members = models.ManyToManyField(to="users.User", through="BoardMemberRelation", related_name="member_boards",
                                     verbose_name="Users who have access to the board. Users have different roles")

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"
