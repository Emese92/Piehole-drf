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


class RecipeDetailViewTests(APITestCase):
    def setUp(self):
        tom = User.objects.create_user(username='tom', password='pass')
        jerry = User.objects.create_user(username='jerry', password='pass')
        Recipe.objects.create(
            owner=tom, title='test', number_of_portions=1
            )
        Recipe.objects.create(
            owner=jerry, title='test2', number_of_portions=1
            )

    def test_can_retrieve_recipe_using_valid_id(self):
        response = self.client.get('/recipes/1/')
        self.assertEqual(response.data['title'], 'test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_not_retrieve_recipe_using_invalid_id(self):
        response = self.client.get('/recipes/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_recipe(self):
        self.client.login(username='tom', password='pass')
        response = self.client.put('/recipes/1/', {
            'title': 'new title',
            'number_of_portions': '1',
            'ingredients': 'eggs',
            'steps': 'Fry eggs'
            })
        recipe = Recipe.objects.filter(pk=1).first()
        self.assertEqual(recipe.title, 'new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_not_update_others_recipe(self):
        self.client.login(username='jerry', password='pass')
        response = self.client.put('/recipes/1/', {
            'title': 'new title',
            'number_of_portions': '1',
            'ingredients': 'eggs',
            'steps': 'Fry eggs'
            })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
