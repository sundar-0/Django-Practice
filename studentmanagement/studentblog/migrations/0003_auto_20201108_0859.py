# Generated by Django 3.1.2 on 2020-11-08 03:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentblog', '0002_auto_20201106_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 8, 8, 59, 25, 93050)),
        ),
    ]