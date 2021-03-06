# Generated by Django 3.1.6 on 2021-02-17 22:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('create_at', models.DateField(default='2021-02-17', verbose_name='Date')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
