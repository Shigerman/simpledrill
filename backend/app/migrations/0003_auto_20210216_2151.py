# Generated by Django 3.1.6 on 2021-02-16 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20210213_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='comment',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='invite',
            name='inviter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invite_issuer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invite',
            name='used_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invite_taker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='challenge_topic',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='disclose_answers',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
