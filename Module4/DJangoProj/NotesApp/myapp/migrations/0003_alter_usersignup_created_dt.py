# Generated by Django 4.1.2 on 2022-11-14 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_feedback_mynotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='created_dt',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 11, 14, 21, 27, 28, 969715)),
        ),
    ]
