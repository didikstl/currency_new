from django.db import models
from app.currency.choices import (
    CurrencyTypeChoices,  # Это вызов через созданный в Choices класс
    SOURCE_TYPE,
    SOURCE_URL_TYPE,
    CURRENCY_PRIVAT,
)


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.SmallIntegerField(
        choices=CurrencyTypeChoices.choices,
        default=CurrencyTypeChoices.USD,
    )
    source = models.CharField(
        max_length=255,
        choices=SOURCE_TYPE,
        default=CURRENCY_PRIVAT
    )

    def __str__(self):
        return f'{self.buy} - {self.sell} - {self.source}'


class ContactUs(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.TextField(verbose_name="subject")
    message = models.TextField(verbose_name="message")


class Source(models.Model):
    source_url = models.URLField(
        max_length=255,
        choices=SOURCE_URL_TYPE,
    )
    source_name = models.CharField(
        max_length=64,
        choices=SOURCE_TYPE,
        default=CURRENCY_PRIVAT
    )
    created = models.DateTimeField(auto_now_add=True)
