# Generated by Django 3.1.2 on 2020-11-08 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentblog', '0006_auto_20201108_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 8, 18, 3, 34, 484542)),
        ),
    ]
