# Generated by Django 4.2.16 on 2024-12-03 03:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0046_alter_event_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 3, 4, 28, 11, 916098, tzinfo=datetime.timezone.utc)),
        ),
    ]
