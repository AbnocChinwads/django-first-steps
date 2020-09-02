from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    def test_done_defailts_to_false(self):
        item = Item.objects.create(name='Test todo item')
        self.assertFalse(item.done)
