# Generated by Django 2.0.4 on 2018-08-02 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 3, 0, 52, 49, 372650))),
            ],
        ),
    ]
