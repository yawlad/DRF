# Generated by Django 3.2.8 on 2022-10-24 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20221024_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_develloper',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_project_holder',
        ),
    ]
