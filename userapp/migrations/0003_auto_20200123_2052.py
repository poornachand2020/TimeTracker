# Generated by Django 2.2.1 on 2020-01-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20200123_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='closetime',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='starttime',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
