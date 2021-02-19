import uuid
from datetime import datetime
from django.db import models

from app.lunch.models import Lunch


def lunchesByMenu(menu_id):
    if isinstance(menu_id, str):
        lunches = []
        lunches_by_menu = Menu.objects.get(id=menu_id).lunches.all()

        for lunch in lunches_by_menu:
            lunches.append((lunch.name, lunch.name))

        return lunches

    return [('', '')]


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    lunches = models.ManyToManyField(Lunch)
    published_at = models.DateField("Date of published", default=datetime.utcnow().strftime('%Y-%m-%d'), unique=True)
    create_at = models.DateField("Date", default=datetime.utcnow().strftime('%Y-%m-%d'))

    class Meta:
        ordering = ['published_at']

    def __str__(self):
        return 'Publish: {} Created: {}'.format(self.published_at, self.create_at)
