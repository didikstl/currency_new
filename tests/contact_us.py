from django.urls import reverse
# - 3

def test_post_contact_us_empty_form(client):
    response = client.post(reverse('message-create'))
    assert response.status_code == 200


def test_contact_us_valid_data(client):
    payload = {
        'name': 'Name',
        'email': 'email@example.com',
        'subject': 'Subject',
        'message': 'Message',
    }
    response = client.post(reverse('message-create'), data=payload)
    assert response.status_code == 302
    assert response.headers['Location'] == '/message/list/'


def test_post_contact_invalid_email(client):
    payload = {
        'name': 'Name',
        'email': 'INVALID_EMAIL',
        'subject': 'Subject',
        'message': 'Message',
    }
    response = client.post(reverse('message-create'), data=payload)

    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Enter a valid email address.']
    }


# import pytest
# from django.core import mail
# from rest_framework.test import APIRequestFactory, force_authenticate
# from app.currency.api.views import ContactUsViewSet
# from app.currency.models import ContactUs
# from app.currency.api.serializers import ContactUsSerializer
# from django.contrib.auth.models import User
# from rest_framework import status
#
# from config import settings


# @pytest.mark.django_db
# class TestContactUsViewSet:
#     def test_create_contact_us(self):
#         factory = APIRequestFactory()
#         view = ContactUsViewSet.as_view({'post': 'create'})
#
#         data = {
#             'name': 'John Doe',
#             'email': 'john.doe@example.com',
#             'subject': 'Test Subject',
#             'message': 'Test Message',
#         }
#
#         request = factory.post('/contact-us/', data)
#         response = view(request)
#
#         assert response.status_code == 201
#
#         contact_us_instance = ContactUs.objects.get(email='john.doe@example.com')
#         assert contact_us_instance is not None
#
#         # Проверка отправленного электронного письма
#         assert len(mail.outbox) == 1
#         sent_mail = mail.outbox[0]
#         assert sent_mail.subject == f"New Contact Us Submission: {data['subject']}"
#         assert sent_mail.to == [settings.DEFAULT_FROM_EMAIL]
#         assert data['name'] in sent_mail.body
#         assert data['email'] in sent_mail.body
#         assert data['subject'] in sent_mail.body
#         assert data['message'] in sent_mail.body
#
#     def test_search_contact_us(self):
#         # Создание тестовых данных
#         ContactUs.objects.create(name='John Doe', email='john.doe@example.com', subject='Test Subject',
#                                  message='Test Message')
#         ContactUs.objects.create(name='Jane Doe', email='jane.doe@example.com', subject='Another Subject',
#                                  message='Another Message')
#
#         factory = APIRequestFactory()
#         view = ContactUsViewSet.as_view({'get': 'list'})
#
#         # Поиск по имени
#         request = factory.get('/contact-us/', {'search': 'John Doe'})
#         response = view(request)
#
#         assert response.status_code == 200
#         assert len(response.data) == 1
#         assert response.data[0]['name'] == 'John Doe'
#
#         # Поиск по электронной почте
#         request = factory.get('/contact-us/', {'search': 'jane.doe@example.com'})
#         response = view(request)
#
#         assert response.status_code == 200
#         assert len(response.data) == 1
#         assert response.data[0]['name'] == 'Jane Doe'
