# Generated by Django 3.1.5 on 2021-05-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20210521_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoform',
            name='date',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]
