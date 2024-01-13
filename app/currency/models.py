import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from app.currency.choices import (
    CurrencyTypeChoices,  # Это вызов через созданный в Choices класс
    SOURCE_TYPE,
    SOURCE_URL_TYPE,
    CURRENCY_PRIVAT,
)
from django.contrib.auth.models import AbstractUser

from django.templatetags.static import static


# RATE _________________________________________________________________________
class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=6, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=6, decimal_places=2)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    # type = models.CharField(_('Type'),
    #                         max_length=50,
    #                         choices=CurrencyTypeChoices.choices,
    #                         default=CurrencyTypeChoices.USD,)
    type = models.SmallIntegerField(
        _('Type'),
        choices=CurrencyTypeChoices.choices,
        default=CurrencyTypeChoices.USD,
    )
    # type = models.CharField(
    #     _('Type'),
    #     choices=CurrencyTypeChoices,
    #     default=CurrencyTypeChoices.USD,
    # )
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


# ContactUs_______________________________________________
class ContactUs(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=64,
        default='admin'
    )
    email = models.EmailField(
        _('Email'),
        max_length=254,
        default='bond007@gmail.com'
    )
    subject = models.CharField(
        _('Subject'),
        max_length=254,
    )
    message = models.CharField(
        _('Message'),
        max_length=254
    )

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')


# Source______________________________________________________
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

    code_name = models.CharField(
        _('Code name'),
        max_length=64,
        unique=True
    )


    created = models.DateTimeField(_('Created'), auto_now_add=True)
    logo = models.FileField(
        _('Logo'),
        default=None,
        null=True,
        blank=True,
        upload_to='logo/'
    )

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')

    @property
    def logo_url(self) -> str:
        if self.logo:
            return self.logo.url

        return static('Privat.png')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = uuid.uuid4()

        return super().save(*args, **kwargs)


# RequestResponseLog______________________________________________

class RequestResponseLog(models.Model):
    path = models.CharField(
        _('Path'),
        max_length=256,
    )
    request_method = models.CharField(
        _('Request method'),
        max_length=256,
    )

    time = models.FloatField(
        _('Time'),
    )

# USER_________________________________________________________________________________
