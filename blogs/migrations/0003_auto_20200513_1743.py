# Generated by Django 3.0.6 on 2020-05-13 10:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200513_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 10, 43, 17, 774813, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 10, 43, 17, 774813, tzinfo=utc)),
        ),
    ]
