# Generated by Django 3.1.3 on 2023-02-09 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20230208_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ManyToManyField(to='onlinecourse.Course'),
        ),
    ]
