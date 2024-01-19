import django_filters

from app.currency.models import Rate, Source, ContactUs


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        # fields = {
        #     'buy': ['exact', 'gt', 'gte', 'lt', 'lte'],
        #     'sell': ['exact', 'gt', 'gte', 'lt', 'lte'],
        #     'type': ['exact'],
        # }
        fields = (
            'buy',
            'sell',
            'type',
        )


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'subject',
            'message',

        )


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'source_name',
        )
