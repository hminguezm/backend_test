# Generated by Django 3.1.6 on 2021-02-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20210219_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='create_at',
            field=models.DateField(default='2021-02-21', verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='published_at',
            field=models.DateField(default='2021-02-21', unique=True, verbose_name='Date of published'),
        ),
    ]