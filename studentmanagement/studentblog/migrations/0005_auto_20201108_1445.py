# Generated by Django 3.1.2 on 2020-11-08 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentblog', '0004_auto_20201108_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 8, 14, 45, 23, 69342)),
        ),
    ]
