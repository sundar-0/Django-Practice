# Generated by Django 3.1.2 on 2020-11-10 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentblog', '0011_auto_20201110_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 16, 28, 53, 399637)),
        ),
    ]