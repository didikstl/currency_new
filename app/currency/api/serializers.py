from rest_framework import serializers

from app.currency.models import Rate, Source, ContactUs


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sell',
            'created',
            'type',
            'source',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'source_url',
            'source_name',
            'created',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'name',
            'email',
            'subject',
            'message',
        )
