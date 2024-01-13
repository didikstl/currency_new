from celery import shared_task
import requests

from app.currency.models import Rate, Source
from app.currency.choices import CurrencyTypeChoices
from app.currency.constants import PRIVATBANK_CODE_NAME
from app.currency.utils import to_2_places_decimal

import logging

logger = logging.getLogger(__name__)


@shared_task
def parse_privatbank():
    try:
        url_privat = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
        response_privat = requests.get(url_privat)
        response_privat.raise_for_status()

        source = Source.objects.filter(code_name='Bank PRIVAT').first()

        if source is None:
            source = Source.objects.create(source_name='Bank PRIVAT', code_name='Bank PRIVAT')

        rates_privat = response_privat.json()

        available_currency_types = {
            'USD': CurrencyTypeChoices.USD,
            'EUR': CurrencyTypeChoices.EUR,
        }

        for rate in rates_privat:
            buy = to_2_places_decimal(rate['buy'])
            sell = to_2_places_decimal(rate['sale'])
            type = rate['ccy']

            if type not in available_currency_types:
                continue

            type = available_currency_types[type]
            last_rate = Rate.objects.filter(source=source, type=type).order_by('-created').first()

            if last_rate is None or (last_rate.buy != buy or last_rate.sell != sell):
                Rate.objects.create(
                    buy=buy,
                    sell=sell,
                    type=type,
                    source=source
                )
    except Exception as e:
        logger.error(f"Error in parse_privatbank: {e}")
        raise


@shared_task
def parse_monobank():
    try:
        url_mono = 'https://api.monobank.ua/bank/currency'
        response_mono = requests.get(url_mono)
        response_mono.raise_for_status()

        source = Source.objects.filter(code_name='Bank MONO').first()

        if source is None:
            source = Source.objects.create(source_name='Bank MONO', code_name='Bank MONO')

        rates_mono = response_mono.json()

        available_currency_types = {
            840: CurrencyTypeChoices.USD,
            978: CurrencyTypeChoices.EUR,
        }

        for rate in rates_mono:
            buy = rate.get('rateBuy')
            sell = rate.get('rateSell')
            type = rate.get('currencyCodeA')

            if type not in available_currency_types:
                continue

            Rate.objects.create(
                buy=buy,
                sell=sell,
                type=type,
                source=source
            )

            type = available_currency_types[type]
            last_rate = Rate.objects.filter(source=source, type=type).order_by('-created').first()

            if last_rate is None or (last_rate.buy != buy or last_rate.sell != sell):
                Rate.objects.create(
                    buy=buy,
                    sell=sell,
                    type=type,
                    source=source
                )

    except Exception as e:
        logger.error(f"Error in parse_monobank: {e}")
        raise
