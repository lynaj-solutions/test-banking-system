

from rest_framework import serializers

from django.conf import settings

from apps.currencies.models import Currency


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = [
            "abbreviation",
            "name"
        ]

