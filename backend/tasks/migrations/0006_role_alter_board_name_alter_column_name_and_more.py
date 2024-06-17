# Generated by Django 5.0.6 on 2024-06-17 18:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_board_user_remove_column_user_board_owner_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('can_drag_tasks', models.BooleanField(default=False, verbose_name='Can drag tasks between columns')),
                ('can_manage_own_tasks', models.BooleanField(default=False, verbose_name='Can create, edit and delete only own tasks')),
                ('can_manage_all_tasks', models.BooleanField(default=False, verbose_name='Can edit and delete all tasks')),
                ('can_manage_columns', models.BooleanField(default=False, verbose_name='Can create, edit and delete all columns')),
                ('can_manage_board', models.BooleanField(default=False, verbose_name='Can edit board but not delete it')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='column',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.CreateModel(
            name='BoardMemberRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_users', to='tasks.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_users', to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_users', to='tasks.role')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='board',
            name='members',
            field=models.ManyToManyField(related_name='member_boards', through='tasks.BoardMemberRelation', to=settings.AUTH_USER_MODEL, verbose_name='Users who have access to the board. Users have different roles'),
        ),
    ]