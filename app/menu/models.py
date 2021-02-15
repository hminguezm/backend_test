import uuid
from datetime import datetime

from django.db import models


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    options = models.CharField(max_length=100)
    date = models.DateField("Date", default=datetime.utcnow())
