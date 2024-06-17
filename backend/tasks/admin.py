from django.contrib import admin

from tasks.models import Board, Task, Column, BoardMemberRelation, Role


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(BoardMemberRelation)
class BoardMemberRelationAdmin(admin.ModelAdmin):
    pass
