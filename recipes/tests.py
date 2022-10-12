from django.contrib.auth.models import User
from .models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase

# These tests were created based on the example project of Code Institute


class RecipeListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='tomas', password='pass')

    def test_can_list_recipes(self):
        tomas = User.objects.get(username='tomas')
        Recipe.objects.create(owner=tomas, title='test', number_of_portions=1)
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_recipe(self):
        self.client.login(username='tomas', password='pass')
        response = self.client.post(
            '/recipes/', {
                'title': 'test',
                'number_of_portions': '1',
                'ingredients': 'eggs',
                'steps': 'Fry eggs'
                }
            )
        count = Recipe.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_can_not_create_recipe(self):
        response = self.client.post(
            '/recipes/', {
                'title': 'test',
                'number_of_portions': '1',
                'ingredients': 'eggs',
                'steps': 'Fry eggs'
                }
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
