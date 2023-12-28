from django import forms

from app.currency.models import Rate, ContactUs, Source


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sell',
            'type',
            'source',
        )


class MessageForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'source_name',
            'logo',
        )
