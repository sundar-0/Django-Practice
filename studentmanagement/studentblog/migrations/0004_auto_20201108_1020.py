# Generated by Django 3.1.2 on 2020-11-08 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentblog', '0003_auto_20201108_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 8, 10, 20, 42, 969590)),
        ),
    ]
