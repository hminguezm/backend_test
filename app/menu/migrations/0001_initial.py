# Generated by Django 3.1.6 on 2021-02-15 22:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('options', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]