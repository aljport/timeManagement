# Generated by Django 4.2.16 on 2024-11-27 05:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0012_alter_event_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 27, 6, 30, 17, 101269, tzinfo=datetime.timezone.utc)),
        ),
    ]
