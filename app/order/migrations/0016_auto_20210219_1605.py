# Generated by Django 3.1.6 on 2021-02-19 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20210218_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2021, 2, 19, 16, 5, 11, 400364), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='meal',
            field=models.CharField(choices=[], max_length=100),
        ),
    ]
