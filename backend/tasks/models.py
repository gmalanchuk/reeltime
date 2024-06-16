from django.db import models


class AbsTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Board(AbsTimeStampModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    user_id = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="boards", verbose_name="Owner")
    # users = пользователи, у которых есть доступ к этой доске (могут создавать, редактировать таски, колонки)

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"


# RELATED_NAME
