import pytest
from django.test import Client
from django.urls import reverse_lazy


@pytest.fixture
def client():
    yield Client()


def test_home_view(client):
    home_url = reverse_lazy('core:home')
    response = client.get(home_url)
    assert response.status_code == 200


def test_about_view(client):
    about_url = reverse_lazy('core:about')
    response = client.get(about_url)
    assert response.status_code == 200
