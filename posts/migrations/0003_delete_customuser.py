# Generated by Django 4.0.2 on 2022-02-17 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
