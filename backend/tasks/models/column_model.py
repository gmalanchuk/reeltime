from django.db import models

from tasks.models import AbsTimeStampModel, Board


class Column(AbsTimeStampModel):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, null=True, blank=True)
    board = models.ForeignKey(to=Board, on_delete=models.CASCADE, related_name="columns")
    owner = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="columns")

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"
