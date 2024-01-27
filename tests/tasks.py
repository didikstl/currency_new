from app.currency.choices import CurrencyTypeChoices
from app.currency.tasks import parse_privatbank, parse_monobank
from unittest.mock import MagicMock
from app.currency.models import Source, Rate


# - 2

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
