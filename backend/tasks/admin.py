from django.contrib import admin

from tasks.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass
