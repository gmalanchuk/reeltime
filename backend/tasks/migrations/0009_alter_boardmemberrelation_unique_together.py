# Generated by Django 5.0.6 on 2024-06-23 08:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_role_can_change_executor_role_can_create_tasks'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='boardmemberrelation',
            unique_together={('user', 'board')},
        ),
    ]
