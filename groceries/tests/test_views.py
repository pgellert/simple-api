import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import GroceryItem
from ..serializers import GroceryItemSerializer


# initialize the APIClient app
client = Client()


class GetAllGroceries(TestCase):
    """ Test module for GET all groceries API """

    def setUp(self):
        GroceryItem.objects.create(
            name='milk', amount=2, msg='for cake')
        GroceryItem.objects.create(
            name='egg', amount=12, msg='for cake')
        GroceryItem.objects.create(
            name='apple', amount=4, msg='')
        GroceryItem.objects.create(
            name='cereal', amount=1, msg='')

    def test_get_all_groceries(self):
        # get API response
        response = client.get(reverse('get_post_groceries'))
        # get data from db
        groceries = GroceryItem.objects.all()
        serializer = GroceryItemSerializer(groceries, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleGroceryItemTest(TestCase):
    """ Test module for GET single grocery item API """

    def setUp(self):
        self.milk = GroceryItem.objects.create(
            name='milk', amount=2, msg='for cake')
        self.egg = GroceryItem.objects.create(
            name='egg', amount=12, msg='for cake')
        self.apple = GroceryItem.objects.create(
            name='apple', amount=4, msg='')
        self.cereal = GroceryItem.objects.create(
            name='cereal', amount=1, msg='')

    def test_get_valid_single_grocery(self):
        response = client.get(
            reverse('get_delete_update_grocery', kwargs={'pk': self.egg.pk}))
        groceryItem = GroceryItem.objects.get(pk=self.egg.pk)
        serializer = GroceryItemSerializer(groceryItem)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_grocery(self):
        response = client.get(
            reverse('get_delete_update_grocery', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewGroceryItemTest(TestCase):
    """ Test module for inserting a new item to the grocery list """

    def setUp(self):
        self.valid_payload = {
            'name': 'milk',
            'amount': 1,
            'msg': '',
        }

        self.invalid_payload = {
            'name': '',
            'amount': 2,
            'msg': 'needed for the cake',
        }

    def test_create_valid_grocery_item(self):
        response = client.post(
            reverse('get_post_groceries'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_grocery_item(self):
        response = client.post(
            reverse('get_post_groceries'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleGroceryItemTest(TestCase):
    """ Test module for updating an existing grocery item """

    def setUp(self):
        self.milk = GroceryItem.objects.create(
            name='milk', amount=2, msg='for cake')
        self.egg = GroceryItem.objects.create(
            name='egg', amount=12, msg='for cake')
        self.valid_payload = {
            'name': 'milk',
            'amount': 1,
            'msg': '',
        }

        self.invalid_payload = {
            'name': '',
            'amount': 2,
            'msg': 'needed for the cake',
        }

    def test_valid_update_grocery_item(self):
        response = client.put(
            reverse('get_delete_update_grocery', kwargs={'pk': self.milk.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_grocery_item(self):
        response = client.put(
            reverse('get_delete_update_grocery', kwargs={'pk': self.milk.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleGroceryItemTest(TestCase):
    """ Test module for deleting an existing grocery item record """

    def setUp(self):
        self.milk = GroceryItem.objects.create(
            name='milk', amount=2, msg='for cake')
        self.egg = GroceryItem.objects.create(
            name='egg', amount=12, msg='for cake')

    def test_valid_delete_grocery(self):
        response = client.delete(
            reverse('get_delete_update_grocery', kwargs={'pk': self.milk.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_grocery(self):
        response = client.delete(
            reverse('get_delete_update_grocery', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
