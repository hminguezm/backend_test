import uuid
from datetime import datetime

from django.db import models


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    applicant_name = models.CharField(max_length=20)
    meal = models.CharField(
        max_length=100,
        choices=[],
    )
    comment = models.TextField(max_length=100)
    create_at = models.DateField("Date", default=datetime.utcnow())
