# Generated by Django 2.0.6 on 2018-07-20 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
