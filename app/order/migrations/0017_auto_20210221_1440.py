# Generated by Django 3.1.6 on 2021-02-21 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20210219_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2021, 2, 21, 14, 40, 32, 445696), verbose_name='Date'),
        ),
    ]
