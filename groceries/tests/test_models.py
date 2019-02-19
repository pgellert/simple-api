from django.test import TestCase
from ..models import GroceryItem


class GroceryItemTest(TestCase):
    """ Test module for GroceryItem model """

    def setUp(self):
        GroceryItem.objects.create(
            name='milk', amount=2, msg='for cake')
        GroceryItem.objects.create(
            name='egg', amount=12, msg='for cake')

    def test_grocery_item(self):
        grocery_item_milk = GroceryItem.objects.get(name='milk')
        grocery_item_egg = GroceryItem.objects.get(name='egg')
        self.assertEqual(
            grocery_item_milk.get_item(), "You need 2 of milk (for cake).")
        self.assertEqual(
            grocery_item_egg.get_item(), "You need 12 of egg (for cake).")
