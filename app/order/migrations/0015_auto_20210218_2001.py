# Generated by Django 3.1.6 on 2021-02-18 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20210218_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2021, 2, 18, 20, 1, 59, 935233), verbose_name='Date'),
        ),
    ]