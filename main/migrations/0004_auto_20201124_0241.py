# Generated by Django 3.1.2 on 2020-11-24 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201124_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 2, 41, 18, 655418), verbose_name='date published'),
        ),
    ]