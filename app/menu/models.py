import uuid
from datetime import datetime
from django.db import models

from app.lunch.models import Lunch


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    lunches = models.ManyToManyField(Lunch)
    published_at = models.DateField("Date of published", default=datetime.utcnow().strftime('%Y-%m-%d'))
    create_at = models.DateField("Date", default=datetime.utcnow().strftime('%Y-%m-%d'))

    class Meta:
        ordering = ['published_at']

    def __str__(self):
        return 'Publish: {} Created: {}'.format(self.published_at, self.create_at)
