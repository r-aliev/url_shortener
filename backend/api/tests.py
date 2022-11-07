from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import URLMapper


class URLMapperTests(APITestCase):
    def test_correct_shorten_url(self):
        """Test correct formatted urls"""
        url = reverse('add_url')
        data = {
            'original_url': 'https://www.djangoproject.com/'
        }
        response = self.client.post(url, data, format='json')

        url_exist = False
        try:
            url_exist = bool(URLMapper.objects.get(original_url=data['original_url']))
        except URLMapper.DoesNotExist:
            pass

        self.assertEqual(url_exist, True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_false_shorten_url(self):
        """Test false formatted URL"""
        url = reverse('add_url')
        data = {
            'original_url': 'dwnenewjfwefn'
        }

        response = self.client.post(url, data, format='json')

        url_exist = False
        try:
            url_exist = bool(URLMapper.objects.get(original_url=data['original_url']))
        except URLMapper.DoesNotExist:
            pass

        self.assertEqual(url_exist, False)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_urls(self):
        """Test get urls method"""
        url = reverse('get_urls')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
