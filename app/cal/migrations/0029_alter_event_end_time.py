# Generated by Django 4.2.16 on 2024-11-17 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0028_alter_event_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 17, 7, 4, 5, 604936, tzinfo=datetime.timezone.utc)),
        ),
    ]
