# from celery import shared_task
# import requests
#
# from app.currency.models import Rate, Source
# from app.currency.choices import CurrencyTypeChoices
#
#
# @shared_task
# def parse_privatbank():
#     url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
#     response = requests.get(url)
#     response.raise_for_status()
#
#     source = Source.objects.create(source_name='PrivatBank')
#
#     rates = response.json()
#
#     available_currency_types = {
#         'USD': CurrencyTypeChoices.USD,
#         'EUR': CurrencyTypeChoices.EUR,
#     }
#
#     for rate in rates:
#         buy = rate['buy']
#         sell = rate['sale']
#         currency_type = rate['ccy']
#
#         if currency_type not in available_currency_types:
#             continue
#
#         currency_type = available_currency_types[currency_type]
#
#         Rate.objects.create(
#             buy=buy,
#             sell=sell,
#             currency_type=currency_type,
#             source=source
#         )
