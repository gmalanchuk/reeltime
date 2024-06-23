from django.db import models


class AbsTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Board(AbsTimeStampModel):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, null=True, blank=True)
    # status = CharField
    owner = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="boards")
    members = models.ManyToManyField(to="users.User", through="BoardMemberRelation", related_name="member_boards", verbose_name="Users who have access to the board. Users have different roles")

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"


class Column(AbsTimeStampModel):
    name = models.CharField(max_length=128)
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


class BoardMemberRelation(AbsTimeStampModel):
    user = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="board_users")
    board = models.ForeignKey(to="Board", on_delete=models.CASCADE, related_name="board_users")
    role = models.ForeignKey(to="Role", on_delete=models.CASCADE, related_name="board_users")

    class Meta:
        unique_together = ('user', 'board')

    def __str__(self):
        return f"ID: {self.pk} | User: {self.user} | Board ID: {self.board.pk} | Role Name: {self.role.name}"


class Role(AbsTimeStampModel):
    """
    This model represents a Role in the system. Each role has a set of permissions.
    When a permission is granted (set to True), all permissions that are listed before it
    in the order of Boolean fields in the model are also granted (set to True). This is to ensure
    that granting a higher-level permission automatically grants all lower-level permissions
    """

    # TODO when creating a board, four roles will be created by default (guest, user, moderator, administrator)
    # TODO create additional fields for more thorough customization

    name = models.CharField(max_length=64)

    # GUEST. all fields are nullable. can only view the board and tasks

    # USER (может только менять поле column_id у всех(не только своих) тасок)
    can_drag_tasks = models.BooleanField(default=False, verbose_name="Can drag tasks between columns")
    can_change_executor = models.BooleanField(default=False, verbose_name="Can change executor of the task")
    can_create_tasks = models.BooleanField(default=False, verbose_name="Can create tasks. Can manage only own tasks(edit and delete)")

    # MODERATOR
    # can_manage_all_tasks = models.BooleanField(default=False, verbose_name="Can edit and delete all tasks")

    # ADMINISTRATOR
    # can_manage_columns = models.BooleanField(default=False, verbose_name="Can create, edit and delete all columns")
    # can_manage_board = models.BooleanField(default=False, verbose_name="Can edit board but not delete it")\

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.name}"

    def save(self, *args, **kwargs):
        """
        When a permission is granted (set to True), all permissions that are listed before it
        in the order of Boolean fields in the model are also granted (set to True)
        """
        fields = [f.name for f in self._meta.get_fields() if isinstance(f, models.BooleanField)]
        for i in range(len(fields) - 1, -1, -1):
            if getattr(self, fields[i]):
                for j in range(i - 1, -1, -1):
                    setattr(self, fields[j], True)
                break

        super().save(*args, **kwargs)
