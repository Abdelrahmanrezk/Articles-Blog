# Generated by Django 2.1.4 on 2018-12-24 17:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 24, 17, 1, 16, 894927, tzinfo=utc)),
        ),
    ]
