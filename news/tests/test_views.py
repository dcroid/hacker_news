from rest_framework import status
from rest_framework.test import APITestCase

from django.core import management


class ApiTests(APITestCase):

    def setUp(self):
        management.call_command('get_news')

        url = '/posts'

        self.response = self.client.get(url, format='json')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_default_limit_size(self):
        result = self.response.data.get('results')
        self.assertEqual(len(result), 5)
