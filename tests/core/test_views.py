from django.test import TestCase, Client
from django.urls import reverse_lazy


class TestCoreViews(TestCase):

    def setUp(self):
        self.home_url = reverse_lazy('core:home')
        self.about_url = reverse_lazy('core:about')
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
