from django.db import models


class AbsTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Board(AbsTimeStampModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="boards", verbose_name="Board owner")
    # TODO users = пользователи, у которых есть доступ к этой доске (могут создавать, редактировать таски, колонки)
    # TODO тоесть админ может редактировать, удалять и тд колонки, какой-то ещё юзер может только создавать таски, другой юзер может только просматривать и перетягивать таски

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"


class Column(AbsTimeStampModel):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(to=Board, on_delete=models.CASCADE, related_name="columns")
    user = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="columns", verbose_name="Column owner")

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"
