import pytest
from django.core.management import call_command
import json


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    :param db:
    :return:
    """


@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient
    client = APIClient()
    yield client


@pytest.fixture(scope='function')
def api_client_auth(django_user_model):
    """
    Эта фикстура предоставляет аутентифицированный APIClient для использования в тестах,
    позволяя отправлять аутентифицированные запросы к API.
    :param django_user_model:
    :return:
    """
    from rest_framework.test import APIClient
    client = APIClient()

    email = 'email@example.com'
    password = 'superSecretPassword'
    user = django_user_model(email=email)
    user.set_password(password)
    user.save()

    # token_response = client.post(
    #     '/api/account/token/',
    #     data={'email': email, 'password': password}
    # )
    # assert token_response.status_code == 200
    # access_token = token_response.json()['access']
    # client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    client.force_authenticate(user=user)

    yield client

    user.delete()

# # предоставления начальных данных перед запуском тестов, чтобы тесты могли использовать фиксированные данные
# @pytest.fixture(scope='session', autouse=True)
# #  фикстура будет жить в течение всей сессии тестирования
# #  (то есть, будет создана и использована один раз для всех тестов).
# def load_fixtures(django_db_setup, django_db_blocker):
#     with django_db_blocker.unblock():
#         # икстура Django для управления блокировкой базы данных.
#         # Она используется для предотвращения одновременного доступа к базе данных из разных потоков/процессов.
#         fixtures = (
#             'sources.json',
#             'rate.json'
#         )
#         for fixture in fixtures:
#             call_command('loaddata', f'tests/fixtures/{fixture}')


# @pytest.fixture(scope='session', autouse=True)
# def load_fixtures(django_db_setup, django_db_blocker):
#     with django_db_blocker.unblock():
#         fixtures = (
#             'sources.json',
#             'rate.json'
#         )
#         for fixture in fixtures:
#             with open(f'tests/fixtures/{fixture}', 'r', encoding='utf-8') as f:
#                 call_command('loaddata',
#                              f'-', **{'input': f, 'format': 'json', 'use_natural_primary_keys': True,
#                                       'ignorenonexistent': False, 'verbosity': 0})
