# Generated by Django 4.2.16 on 2024-11-17 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0024_alter_event_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 17, 6, 43, 13, 30596, tzinfo=datetime.timezone.utc)),
        ),
    ]
