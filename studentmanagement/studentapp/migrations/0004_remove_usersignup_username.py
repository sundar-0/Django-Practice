# Generated by Django 3.1.2 on 2020-11-04 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_auto_20201104_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersignup',
            name='username',
        ),
    ]
