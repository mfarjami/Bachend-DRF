# Generated by Django 3.2 on 2021-04-24 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_todo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='name',
        ),
    ]
