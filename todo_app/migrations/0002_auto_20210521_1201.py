# Generated by Django 3.1.5 on 2021-05-21 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='form',
            new_name='todoform',
        ),
    ]