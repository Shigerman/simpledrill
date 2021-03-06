# Generated by Django 3.1.6 on 2021-03-03 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20210216_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challengesummary',
            name='failed_count',
        ),
        migrations.AddField(
            model_name='challengesummary',
            name='asked_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='invite',
            name='used_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invite_taker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='challenge_topic',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='disclose_answers',
            field=models.BooleanField(null=True),
        ),
    ]
