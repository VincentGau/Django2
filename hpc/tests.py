from django.test import TestCase, override_settings
from django.contrib.staticfiles import finders

# Create your tests here.
from django.urls import reverse

from hpc.models import User


class StaticFileTest(TestCase):
    def test_css_file(self):
        result = finders.find('hpc/css/style.css')
        self.assertNotEqual(result, None)


class HomePageViewTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Index')

    def test_authenticated_page(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_not_authenticated_page(self):
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'login')


class HpcViewsTest(TestCase):
    def test_hpc_home_page(self):
        response = self.client.get(reverse('hpc:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Index')


class AccountViewsTest(TestCase):
    def test_login_page(self):
        response = self.client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'login')


class MultiDomainTest(TestCase):
    @override_settings(ALLOWED_HOSTS=['www.test.com'])
    def test_other_domain(self):
        response = self.client.get('/', HTTP_HOST='kohaku.cc')
        self.assertEqual(response.status_code, 400)

    @override_settings(ALLOWED_HOSTS=['kohaku.cc'])
    def test_correct_domain(self):
        response = self.client.get('/', HTTP_HOST='kohaku.cc')
        self.assertEqual(response.status_code, 200)