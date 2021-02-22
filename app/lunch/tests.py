from django.test import TestCase

from .models import Lunch


class LunchTestCase(TestCase):
    def setUp(self):
        Lunch.objects.create(name="Coca Cola")
