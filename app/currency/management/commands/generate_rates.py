import random
from django.core.management.base import BaseCommand, CommandError

from app.currency.models import Rate, Source, ContactUs
from app.currency.choices import CurrencyTypeChoices


class Command(BaseCommand):
    help = "Generates 100 random rates"

    def handle(self, *args, **options):
        source = Source.objects.get_or_create(
            code_name='dummy',
            defaults={
                'source_name': 'Dummy Source'
            }
        )

        for _ in range(500):
            Rate.objects.create(
                buy=random.randint(30, 40),
                sell=random.randint(30, 40),
                type=random.choice(CurrencyTypeChoices.choices)[0],
                source=source,
            )
