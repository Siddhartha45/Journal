# Generated by Django 4.1 on 2024-07-11 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signal_app', '0003_rename_customuser_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
