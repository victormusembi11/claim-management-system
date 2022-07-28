from django.test import TestCase
from django.urls import reverse


class TestCoreAppView(TestCase):

    def setUp(self):
        self.home_url = reverse('core:home')
        self.about_url = reverse('core:about')
        return super().setUp()

    def test_home_view_success(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_about_view_success(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
