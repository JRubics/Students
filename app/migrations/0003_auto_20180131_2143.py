# Generated by Django 2.0.1 on 2018-01-31 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]