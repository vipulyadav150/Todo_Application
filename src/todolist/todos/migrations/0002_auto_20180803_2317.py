# Generated by Django 2.0.4 on 2018-08-03 17:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.OneToOneField(default='vipul', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 3, 23, 17, 36, 248574)),
        ),
    ]
