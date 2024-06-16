from django.db import models


class AbsTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Board(AbsTimeStampModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # user_id = айди создателя доски
    # columns = related field (обратное поле)
    # users = related field (обратное поле)

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"
