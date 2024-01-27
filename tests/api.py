# from django.urls import reverse
# from rest_framework.test import APIClient
#
# from app.currency.models import Source
#
#
# def test_get_rate_list(api_client):
#     response = api_client.get(reverse('rate-list'))
#     assert response.status_code == 302
#     # assert response.json()
#
#
# def test_post_rate_list(api_client):
#     source = Source.objects.create(source_name='Test', code_name='test')
#     payload = {
#         'buy': '37.00',
#         'sell': '38.00',
#         'source': source.id
#     }
#     response = api_client.post(reverse('rate-list'), data=payload)
#     assert response.status_code == 302
