from django.test import TestCase, Client
from django.urls import reverse


class TestAccountViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_login_view(self):
        url = reverse('accounts:login')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
