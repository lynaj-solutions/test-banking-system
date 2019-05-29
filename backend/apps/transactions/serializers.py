from rest_framework import serializers

from django.conf import settings

from generic_relations.relations import GenericRelatedField

from datetime import date
import json
import re

from apps.transactions.models import *
from apps.misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)

class TransactionSerializer(serializers.ModelSerializer):
    recipient = serializers.SerializerMethodField()
    sender = serializers.SerializerMethodField()
    fromc = serializers.SerializerMethodField()
    toc = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = [
            'recipient',
            'sender',
            'fromc',
            'toc',
            'value',
            'rate',
            'created_at',
            'updated_at',
            'status'
        ]


    def get_status(self, instance):
        currency = None
        try:
            currency = re.split("[^a-zA-Z]*", instance.transactionStatusChoices)[1]
        except Exception as e:
            currency = 1.0

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_status: "
                + '\n'
                + str(e)
            )
        return currency

    def get_rate(self, instance):
        currency = None
        try:
            currency = instance.exchangeRate
        except Exception as e:
            currency = 1.0

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_rate: "
                + '\n'
                + str(e)
            )
        return currency

    def get_recipient(self, instance):
        currency = None
        try:
            currency = instance.recipient.userObject.email
        except Exception as e:
            currency = ""

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_recipient: "
                + '\n'
                + str(e)
            )
        return currency

    def get_sender(self, instance):
        currency = None
        try:
            currency = instance.sender.userObject.email
        except Exception as e:
            currency = ""

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_recipient: "
                + '\n'
                + str(e)
            )
        return currency

    def get_fromc(self, instance):
        currency = None
        try:
            currency = instance.fromCurrency.abbreviation
        except Exception as e:
            currency = ""

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_fromc: "
                + '\n'
                + str(e)
            )
        return currency

    def get_toc(self, instance):
        currency = None
        try:
            currency = instance.toCurrency.abbreviation
        except Exception as e:
            currency = ""

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_toc: "
                + '\n'
                + str(e)
            )
        return currency

class TransactionAnonymousSerializer(serializers.ModelSerializer):
    recipient = serializers.SerializerMethodField()
    sender = serializers.SerializerMethodField()
    fromc = serializers.SerializerMethodField()
    toc = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = [
            'recipient',
            'sender',
            'fromc',
            'toc',
            'value',
            'rate',
            'created_at',
            'updated_at',
            'status'
        ]


    def get_status(self, instance):
        currency = None
        try:
            currency = re.split("[^a-zA-Z]*", instance.transactionStatusChoices)[1]
        except Exception as e:
            currency = 1.0

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_status: "
                + '\n'
                + str(e)
            )
        return currency

    def get_rate(self, instance):
        currency = None
        try:
            currency = instance.exchangeRate
        except Exception as e:
            currency = 1.0

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_rate: "
                + '\n'
                + str(e)
            )
        return currency

    def get_recipient(self, instance):
        field = "*****"
        return field

    def get_sender(self, instance):
        field = "*****"
        return field

    def get_fromc(self, instance):
        currency = None
        try:
            currency = instance.fromCurrency.abbreviation
        except Exception as e:
            currency = ""

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_fromc: "
                + '\n'
                + str(e)
            )
        return currency

    def get_toc(self, instance):
        currency = None
        try:
            currency = instance.toCurrency.abbreviation
        except Exception as e:
            currency = ""

            logger.error(
                "Something unexpected happened when in: TransactionSerializer-get_toc: "
                + '\n'
                + str(e)
            )
        return currency


recipient = models.ForeignKey(
    Client,
    null=False,
    on_delete=models.CASCADE,
    verbose_name='Recipient of the transaction',
    related_name="transaction_recipient"
)

sender = models.ForeignKey(
    Client,
    null=False,
    on_delete=models.CASCADE,
    verbose_name='Creator of the transaction',
    related_name='transaction_sender'
)

fromCurrency = models.ForeignKey(
    Currency,
    null=False,
    on_delete=models.CASCADE,
    verbose_name='From currency of the transaction',
    related_name="transaction_from_currency"
)

toCurrency = models.ForeignKey(
    Currency,
    null=False,
    on_delete=models.CASCADE,
    verbose_name='Tocurrency of the transaction',
    related_name="transaction_to_currency"
)

value = models.DecimalField(
    default=0.0,
    max_digits=190,
    null=False,
    decimal_places=4,
    verbose_name='Value of the transaction denoted in from currency'
)

exchangeRate = models.DecimalField(
    default=0.0,
    max_digits=190,
    null=False,
    decimal_places=4,
    verbose_name='Ratio of currencies used in the transaction'
)

created_at = models.DateTimeField(
    verbose_name='Created at',
    auto_now_add=timezone.now
)

transactionStatusChoices = models.CharField(
    choices=TransactionStatusChoices,
    default=next(iter(TransactionStatusChoices))[0],
    max_length=300,
    null=False,
    verbose_name='Status of the transaction'
)

updated_at = models.DateTimeField(
    verbose_name='Updated at',
    blank=True,
    auto_now_add=timezone.now
)
