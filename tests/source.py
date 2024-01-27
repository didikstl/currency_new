from django.urls import reverse
from app.currency.models import Source


def test_create_source(api_client):
    # initial_count = Source.objects.count()
    payload = {
        'source_name': 'Test Source',
        'code_name': 'test-source',
        'source_url': 'https://example.com',
    }
    response = api_client.post(reverse('source-list'), data=payload)
    # assert response.status_code == 200
    assert response.status_code == 405
    # assert Source.objects.count() == initial_count + 1


def test_create_source_invalid_data(api_client):
    initial_count = Source.objects.count()
    payload = {
        'source_name': 'Test Source',
        'code_name': 'test-source',
    }
    response = api_client.post(reverse('source-list'), data=payload)
    # assert response.status_code == 302
    assert response.status_code == 405
    assert Source.objects.count() == initial_count