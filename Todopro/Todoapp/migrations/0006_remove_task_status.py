# Generated by Django 4.0.4 on 2022-05-19 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todoapp', '0005_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]