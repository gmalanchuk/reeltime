from django.db import models

from tasks.models import AbsTimeStampModel, Column


class Task(AbsTimeStampModel):
    description = models.CharField(max_length=2048)
    column = models.ForeignKey(to=Column, on_delete=models.CASCADE, related_name="tasks")
    owner = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="tasks")
    executor = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="tasks_executor", null=True,
                                 blank=True)

    # deadline
    # priority = choices (low, medium, high)
    # tags
    # story points = choices (1, 2, 3, 5, 8, 13, 21)

    def __str__(self):
        return f"ID: {self.pk} | Description: {self.description[:15]}..."
