from django.contrib import admin

from tasks.models import Board, Task, Column


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
