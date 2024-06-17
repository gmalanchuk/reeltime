from django.db import models


class AbsTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Board(AbsTimeStampModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=512, null=True, blank=True)
    owner = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="boards")
    # TODO users = пользователи, у которых есть доступ к этой доске (могут создавать, редактировать таски, колонки)

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"


class Column(AbsTimeStampModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256, null=True, blank=True)
    board = models.ForeignKey(to=Board, on_delete=models.CASCADE, related_name="columns")
    owner = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="columns")

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"


class Task(AbsTimeStampModel):
    description = models.CharField(max_length=2048)
    column = models.ForeignKey(to=Column, on_delete=models.CASCADE, related_name="tasks")
    owner = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="tasks")
    executor = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="tasks_executor", null=True, blank=True)
    # deadline
    # priority = choices (low, medium, high)
    # tags
    # story points = choices (1, 2, 3, 5, 8, 13, 21)

    def __str__(self):
        return f"ID: {self.pk} | Description: {self.description[:15]}..."
