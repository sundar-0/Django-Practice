# Generated by Django 3.1.2 on 2020-11-04 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_auto_20201104_0921'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserSignup',
        ),
    ]