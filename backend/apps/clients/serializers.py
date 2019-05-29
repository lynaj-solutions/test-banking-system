from rest_framework import serializers

from django.conf import settings

from generic_relations.relations import GenericRelatedField

from datetime import date

from apps.clients.models import *
from apps.misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)

class ClientBalanceSerializer(serializers.ModelSerializer):
    currency = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()

    class Meta:
        model = ClientBalance
        fields = [
            'currency',
            'value'
        ]

    def get_currency(self, instance):
        currency = None
        try:
            currency = instance.balanceCurrency.abbreviation
        except Exception as e:
            currency = ""

            logger.error(
                "Something unexpected happened when in: ClientBalanceSerializer-get_currency: "
                + '\n'
                + str(e)
            )
        return currency

    def get_value(self, instance):
        currency = None
        try:
            currency = instance.balanceValue
        except Exception as e:
            currency = 0.0

            logger.error(
                "Something unexpected happened when in: ClientBalanceSerializer-get_value: "
                + '\n'
                + str(e)
            )
        return currency
