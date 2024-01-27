from unittest.mock import MagicMock

from app.currency.choices import CurrencyTypeChoices


# - 4

# def test_answer():
#     '''
#     Использование префикса "test_" в именах функций тестирования имеет следующие преимущества:
#     Ясность: Префикс делает очевидным, что функция представляет собой тест.
#     Если вы видите функцию с именем, начинающимся с "test_", это сигнализирует о том, что это тест.
#     Автоматизация: Некоторые инструменты для запуска тестов
#     (например, модуль unittest в стандартной библиотеке Python) автоматически обнаруживают и запускают тесты,
#     основываясь на соглашениях именования. Если вы используете префикс "test_",
#     то эти инструменты могут легко определить, какие функции следует рассматривать как тесты.
#     :return:
#     '''
#     assert func(3) == 5


def test_index(client):
    responce = client.get('/')
    assert responce.status_code == 200


def test_get_rate_list(client):
    response = client.get('/rate/list/', follow=True)
    # В Django, при отправке HTTP-запросов с использованием библиотеки requests или аналогичных,
    # параметр follow принимает булево значение и указывает, следует ли следовать перенаправлениям (редиректам)
    # автоматически.
    # Если follow установлен в True, библиотека requests автоматически следует по всем перенаправлениям,
    # пока не достигнет конечной точки (например, успешного ответа или ошибки).
    # Это полезно в ситуациях, когда веб-сервер выполняет перенаправление, например, после успешной аутентификации.
    assert response.status_code == 200


# def test_post_contact_us_empty_form(client):
#     response = client.post(reverse('message-create'))
#     assert response.status_code == 200


# def test_post_contact_invalid_email(client):
#     payload = {
#         'name': 'Name',
#         'email': 'INVALID_EMAIL',
#         'subject': 'Subject',
#         'message': 'Message',
#     }
#     response = client.post(reverse('message-create'), data=payload)
#
#     assert response.status_code == 200
#     assert response.context_data['form'].errors == {
#         'email': ['Enter a valid email address.']
#     }
# breakpoint()


# def test_contact_us_valid_data(client):
#     payload = {
#         'name': 'Name',
#         'email': 'email@example.com',
#         'subject': 'Subject',
#         'message': 'Message',
#     }
#     response = client.post(reverse('message-create'), data=payload)
#     assert response.status_code == 302
#     assert response.headers['Location'] == '/message/list/'


# __________________API_______________________________________________________________

from app.currency.models import Rate

#
#
# # def test_get_rate_list(api_client):
# #     response = api_client.get(reverse('rate-list'))
# #     assert response.status_code == 302
# #     # assert response.json()
#
#
def test_post_rate_list_valid_data(api_client_auth):
    # initial_count = Rate.objects.count()
    source = Source.objects.create(source_name='Test', code_name='test')
    payload = {
        'buy': '37.00',
        'sell': '38.00',
        'source': source.id
    }
    response = api_client_auth.post(reverse('rate-list'), data=payload)
    assert response.status_code == 302
    # assert Rate.objects.count() == initial_count + 1

    # # force_authenticate для аутентификации клиента
    # api_client_auth.force_authenticate(user=None)
    # # Перед аутентификацией происходит сброс старой аутентификацию, чтобы переаутентифицировать пользователя
    # response = api_client_auth.post(reverse('rate-list'), data=payload)
    #
    # assert response.status_code == status.HTTP_201_CREATED
    # assert Rate.objects.count() == initial_count + 1


def test_post_rate_list_invalid_data(api_client_auth):
    source = Source.objects.create(source_name='Test', code_name='test')
    payload = {
        'buy': '37.000',
        'sell': '38.00',
        'source': source.id
    }
    response = api_client_auth.post(reverse('rate-list'), data=payload)
    assert response.status_code == 302
    # Статус-код 302 означает, что запрос был успешно обработан, но сервер хочет,
    # чтобы клиент перешел по другому адресу.
    # Это происходить, при попытке доступа к защищенному ресурсу без предварительной аутентификации.


# ______________def test_parse_privatbank_____________________________
from app.currency.tasks import parse_privatbank, parse_monobank


def test_parse_privatbank(mocker):
    initial_count = Rate.objects.count()
    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.95000", "sale": "41.95000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.60000", "sale": "38.20000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.60000", "sale": "38.20000"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data),
    )
    parse_privatbank()

    assert Rate.objects.count() == initial_count + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args[0][0] == 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'

def test_parse_privatbank_prevent_dublicates(mocker):

    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.95000", "sale": "41.95000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.60000", "sale": "38.20000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.60000", "sale": "38.20000"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data),
    )
    source, created = Source.objects.get_or_create(code_name='Bank PRIVAT', defaults={'source_name': 'PrivatBank'})
    Rate.objects.create(source=source, buy="40.95", sell="41.95", type=CurrencyTypeChoices.EUR)
    Rate.objects.create(source=source, buy="37.60", sell="38.20", type=CurrencyTypeChoices.USD)
    initial_count = Rate.objects.count()
    parse_privatbank()

    assert Rate.objects.count() == initial_count
    assert requests_get_mock.call_count == 1


def test_parse_monobank(mocker):
    initial_count = Rate.objects.count()
    mono_data = [
        {'currencyCodeA': 840, 'rateBuy': 27.5, 'rateSell': 28.0},
        {'currencyCodeA': 978, 'rateBuy': 30.0, 'rateSell': 30.5},
        {'currencyCodeA': 111, 'rateBuy': 30.0, 'rateSell': 30.5},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: mono_data),
    )
    parse_monobank()
    assert Rate.objects.count() == initial_count + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args[0][0] == 'https://api.monobank.ua/bank/currency'


def test_parse_monobank_prevent_dublicates(mocker):
    mono_data = [
        {'currencyCodeA': 840, 'rateBuy': 27.5, 'rateSell': 28.0},
        {'currencyCodeA': 978, 'rateBuy': 30.0, 'rateSell': 30.5},
        {'currencyCodeA': 111, 'rateBuy': 30.0, 'rateSell': 30.5},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: mono_data),
    )
    source, created = Source.objects.get_or_create(code_name='Bank MONO', defaults={'source_name': 'Bank MONO'})
    Rate.objects.create(source=source, buy=27.5, sell=28.0, type=CurrencyTypeChoices.USD)
    Rate.objects.create(source=source, buy=30.0, sell=30.5, type=CurrencyTypeChoices.EUR)

    initial_count = Rate.objects.count()
    parse_monobank()

    assert Rate.objects.count() == initial_count
    assert requests_get_mock.call_count == 1


# ____________________________________________________________________________
# # https://chat.openai.com/
# from unittest.mock import patch
# from django.test import TestCase
# from app.currency.tasks import parse_privatbank, parse_monobank
#
#
# class CurrencyParsingTestCase(TestCase):
#
#     @patch('app.currency.tasks.requests.get')
#     def test_parse_privatbank(self, mock_get):
#         mock_get.return_value.json.return_value = [
#             {'ccy': 'USD', 'buy': 27.5, 'sale': 28.0},
#             {'ccy': 'EUR', 'buy': 30.0, 'sale': 30.5},
#         ]
#         parse_privatbank.delay()
#
#     @patch('app.currency.tasks.requests.get')
#     def test_parse_monobank(self, mock_get):
#         mock_get.return_value.json.return_value = [
#             {'currencyCodeA': 840, 'rateBuy': 27.5, 'rateSell': 28.0},
#             {'currencyCodeA': 978, 'rateBuy': 30.0, 'rateSell': 30.5},
#         ]
#         parse_monobank.delay()


# ___________________source___________________________________________

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


# @pytest.mark.django_db
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
