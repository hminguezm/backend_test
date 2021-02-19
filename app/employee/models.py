import uuid
from datetime import datetime
from django.db import models

from app.constans import COUNTRY_CHOICES


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICES,
        default='CL'
    )
    create_at = models.DateField("Date", default=datetime.utcnow().strftime('%Y-%m-%d'))

    class Meta:
        ordering = ['name']
