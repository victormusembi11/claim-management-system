from django.test import TestCase, Client
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


class TestAuthentication(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='johndoe')
        self.user.set_password('1234')
        self.user.save()

        self.client = Client()

    def test_user_login(self):
        response = self.client.post(
            reverse_lazy('accounts:login'),
            {'username': 'johndoe', 'password': '1234'}
        )
        self.assertTrue(response.status_code == 302)
