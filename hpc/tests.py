from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class HomePageViewTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home Page.')


class HpcViewsTest(TestCase):
    def test_hpc_home_page(self):
        response = self.client.get(reverse('hpc:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'hpc main page.')