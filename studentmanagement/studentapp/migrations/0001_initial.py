# Generated by Django 3.1.2 on 2020-11-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=100)),
                ('stu_roll', models.IntegerField()),
                ('stu_contact', models.IntegerField()),
                ('stu_email', models.EmailField(max_length=100)),
                ('stu_faculty', models.CharField(max_length=100)),
            ],
        ),
    ]
