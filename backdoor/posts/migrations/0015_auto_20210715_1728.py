# Generated by Django 3.2.4 on 2021-07-15 10:28

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0014_auto_20210713_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityonlypost',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 15, 10, 28, 58, 362482, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 15, 10, 28, 58, 360483, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='ReferredPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(validators=[django.core.validators.MinLengthValidator(limit_value=300, message='You probably need more characters')])),
                ('slug', models.SlugField(blank=True, max_length=16, null=True, unique=True)),
                ('posted', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 7, 15, 10, 28, 58, 361483, tzinfo=utc))),
                ('date_posted', models.DateTimeField(blank=True, null=True)),
                ('referred_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.postmodel')),
                ('userdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
