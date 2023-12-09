from django.db import models
from django.utils.translation import gettext_lazy as _
from app.currency.choices import (
    CurrencyTypeChoices,  # Это вызов через созданный в Choices класс
    SOURCE_TYPE,
    SOURCE_URL_TYPE,
    CURRENCY_PRIVAT,
)


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=6, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=6, decimal_places=2)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    type = models.SmallIntegerField(
        _('Type'),
        choices=CurrencyTypeChoices.choices,
        default=CurrencyTypeChoices.USD,
    )
    source = models.CharField(
        _('Source'),
        max_length=255,
        choices=SOURCE_TYPE,
        default=CURRENCY_PRIVAT
    )

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')

    def __str__(self):
        return f'{self.buy} - {self.sell} - {self.source}'


class ContactUs(models.Model):
    email = models.EmailField(_('Email'), max_length=254)
    subject = models.TextField(verbose_name="subject")
    message = models.TextField(verbose_name="message")

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')


class Source(models.Model):
    source_url = models.URLField(

        _('Source URL'),
        max_length=255,
        choices=SOURCE_URL_TYPE,
    )
    source_name = models.CharField(
        _('Source name'),
        max_length=64,
        choices=SOURCE_TYPE,
        default=CURRENCY_PRIVAT
    )
    created = models.DateTimeField(_('Created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')
