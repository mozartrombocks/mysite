# Generated by Django 3.1.2 on 2020-11-26 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20201126_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 4, 5, 2, 62786), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='tutorial_series',
            field=models.CharField(max_length=200),
        ),
    ]