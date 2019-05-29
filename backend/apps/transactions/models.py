from uuid import uuid4

from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import uuid

from apps.clients.models import Client
from apps.currencies.models import Currency, CurrencyRatio

from apps.misc.logger import *
from apps.transactions.choices import TransactionStatusChoices

# +++++++++++++++++++++++++++++++++++
logger = logging.getLogger(__name__)
logger.addHandler(handler)
# +++++++++++++++++++++++++++++++++++


class Transaction(models.Model):
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

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
