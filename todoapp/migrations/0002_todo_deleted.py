# Generated by Django 3.2.8 on 2022-10-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
    ]
