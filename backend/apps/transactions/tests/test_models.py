from apps.currencies.models import *
from apps.users.models import *
from apps.transactions.models import *
from apps.clients.models import *

from apps.currencies.choices import CURRENCY_TYPE
from django.test import TestCase

from misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)


class TransactionsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        '''
            Creating default currencies
            Due to the existence of Trigger locked on Client object,
            this operation has to be completed before
            the creation of the user
        '''

    currencyIterator = iter(CURRENCY_TYPE)
    for currencies in range(len(CURRENCY_TYPE)):
        nextCurrency = next(currencyIterator)
        if (currencies == 0):
            Currency.objects.create(
                name=nextCurrency[0],
                abbreviation=nextCurrency[1],
                defaultSystemCurrency=True
            )
        else:
            Currency.objects.create(
                name=nextCurrency[0],
                abbreviation=nextCurrency[1]
            )

    queriedCurrencies = Currency.objects.all()

    '''
        Making sure that number of created currencies
        matches these stored in choices.py
        '''

    '''
    Creating & setting up test users
    as well as logging in & receiving a JWT token
    '''
    test_first_name__first_user = "Karl"
    test_last_name__first_user = "Mark"
    test_email__first_user = "asd123213johnymarge1@wp.pl"
    test_password__first_user = "ij43i$#@"

    test_first_name__second_user = "Karl2"
    test_last_name__second_user = "Mark2"
    test_email__second_user = "johny12312312marge1@wp2.pl"
    test_password__second_user = "ij43i2$#@"

    User.objects.all().delete()

    test_first_user = User.objects.create_user(
        first_name=test_first_name__first_user,
        last_name=test_last_name__first_user,
        email=test_email__first_user,
        password=test_password__first_user
    )

    test_first_user.is_active = True
    test_first_user.save()

    test_second_user = User.objects.create_user(
        first_name=test_first_name__second_user,
        last_name=test_last_name__second_user,
        email=test_email__second_user,
        password=test_password__second_user
    )



    test_second_user.is_active = True
    test_second_user.save()


    Transaction.objects.create(
        recipient=Client.objects.all()[0],
        sender=Client.objects.all()[1],
        fromCurrency=queriedCurrencies[0],
        toCurrency=queriedCurrencies[0],
        value=13,
    )


def test_recipient_label(self):
    queriedObject = Transaction.objects.get(id=1)
    field_label = queriedObject._meta.get_field('recipient').verbose_name
    self.assertEquals(field_label, 'Recipient of the transaction')


def test_sender_label(self):
    queriedObject = Transaction.objects.get(id=1)
    field_label = queriedObject._meta.get_field('sender').verbose_name
    self.assertEquals(field_label, 'Creator of the transaction')


def test_fromCurrency_label(self):
    queriedObject = Transaction.objects.get(id=1)
    field_label = queriedObject._meta.get_field('fromCurrency').verbose_name
    self.assertEquals(field_label, 'From currency of the transaction')


def test_toCurrency_label(self):
    queriedObject = Transaction.objects.get(id=1)
    field_label = queriedObject._meta.get_field('toCurrency').verbose_name
    self.assertEquals(field_label, 'To currency of the transaction')


def test_value_label(self):
    queriedObject = Transaction.objects.get(id=1)
    field_label = queriedObject._meta.get_field('value').verbose_name
    self.assertEquals(field_label, 'Value of the transaction denoted in from currency')


def test_exchangeRate_label(self):
    queriedObject = Transaction.objects.get(id=1)
    field_label = queriedObject._meta.get_field('exchangeRate').verbose_name
    self.assertEquals(field_label, 'Ratio of currencies used in the transaction')


def test_created_at_label(self):
    queriedObject = Transaction.objects.get(id=1)
    field_label = queriedObject._meta.get_field('created_at').verbose_name
    self.assertEquals(field_label, 'Created at')


def test_transactionStatusChoices_label(self):
    queriedObject = Transaction.objects.get(id=1)
    field_label = queriedObject._meta.get_field('transactionStatusChoices').verbose_name
    self.assertEquals(field_label, 'Status of the transaction')
