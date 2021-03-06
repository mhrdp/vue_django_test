# Generated by Django 3.2.4 on 2021-06-19 05:01

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_membersroom_membersroomresident'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='referred',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='date_created',
            field=models.DateField(default=datetime.date(2021, 6, 19)),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='post',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(limit_value=300, message='You probably need more than that to elaborate yout thought!')]),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='userdata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CommunityOnlyPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_restricted', models.BooleanField(default=False)),
                ('member_tier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.membersroom')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.postmodel')),
            ],
        ),
    ]
