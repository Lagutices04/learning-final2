# Generated by Django 4.2.2 on 2024-03-10 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0006_remove_task_user_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]