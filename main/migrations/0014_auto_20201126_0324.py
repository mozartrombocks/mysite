# Generated by Django 3.1.2 on 2020-11-26 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20201126_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 3, 24, 55, 187807), verbose_name='date published'),
        ),
    ]