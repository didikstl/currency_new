# do not import!!!!
from django.db import models


# CURRENCY_USD = 1
# CURRENCY_EUR = 2
# CURRENCY_UAH = 3
# CURRENCY_PLN = 4
# CURRENCY_TYPE = (
#     (CURRENCY_USD, 'Dollar_USA'),  # первое значение идет в базу, второй для пользователя
#     (CURRENCY_EUR, 'EVRO_Europe'),
#     (CURRENCY_UAH, 'Ukrainian_hryvnia'),
#     (CURRENCY_PLN, 'Polish_zloty'),
#
# )

class CurrencyTypeChoices(models.IntegerChoices):
    USD = 1, 'Dollar_USA'
    EUR = 2, 'EVRO_Europe'
    UAH = 3, 'Ukrainian_hryvnia'
    PLN = 4, 'Polish_zloty'


# class CurrencyTypeChoices(models.CharField):
#     USD = 'USD', 'Dollar_USA'
#     EUR = 'EUR', 'EVRO_Europe'
#     UAH = 'UAH', 'Ukrainian_hryvnia'
#     PLN = 'PLN', 'Polish_zloty'
# ____________'________________________________________________________________________________

CURRENCY_PIVDENNY = 'PIVDENNY'
CURRENCY_PRIVAT = 'PRIVAT'
CURRENCY_CREDITDNEPR = 'CREDITDNEPR'
CURRENCY_MONOBANK = 'MONOBANK'

SOURCE_TYPE = (
    (CURRENCY_PIVDENNY, 'Bank Pivdenny'),  # первое значение идет в базу, второй для пользователя
    (CURRENCY_PRIVAT, 'Bank PRIVAT'),
    (CURRENCY_CREDITDNEPR, 'Bank Credit Dnipro'),
    (CURRENCY_MONOBANK, 'Bank MONO'),
)
# ___________________________________________________________________________________________

# SOURCE_URL_TYPE = (
#     ('https://bank.com.ua/en', 'Bank Pivdenny'),  # первое значение идет в базу, второй для пользователя
#     ('https://en.privatbank.ua/', 'Bank PRIVAT'),
#     # ('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5', 'Bank PRIVAT'),
#     ('https://creditdnepr.com.ua/en', 'Bank Credit Dnipro'),
#     ('https://www.monobank.ua/', 'Bank MONO'),
#
# )

SOURCE_URL_TYPE = (
    ('https://bank.com.ua/en', 'Bank Pivdenny'),  # первое значение идет в базу, второй для пользователя
    ('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5', 'Bank PRIVAT'),
    # ('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5', 'Bank PRIVAT'),
    ('https://creditdnepr.com.ua/en', 'Bank Credit Dnipro'),
    ('https://api.monobank.ua/bank/currency', 'Bank MONO'),

)




# SOURCE_IMAGES = (
#     (CURRENCY_PIVDENNY, 'var/logo/Pi'),
#     (CURRENCY_PRIVAT, 'Bank PRIVAT'),
#     (CURRENCY_CREDITDNEPR, 'Bank Credit Dnipro'),
# )
# # ________________________________________________________________________________________
