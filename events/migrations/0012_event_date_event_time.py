# Generated by Django 4.1.5 on 2023-01-14 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_remove_event_date_remove_event_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 15)),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 1, 15, 2, 52, 47, 366103)),
        ),
    ]