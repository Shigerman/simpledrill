# Generated by Django 3.1.6 on 2021-02-13 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challengesummary',
            old_name='user',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='currentanswers',
            old_name='user',
            new_name='person',
        ),
        migrations.RenameField(
            model_name='testsummary',
            old_name='user',
            new_name='person',
        ),
    ]
