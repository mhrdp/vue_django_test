# Generated by Django 3.2.4 on 2021-07-11 07:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20210710_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityonlypost',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 11, 7, 26, 28, 446524, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 11, 7, 26, 28, 430899, tzinfo=utc)),
        ),
    ]
