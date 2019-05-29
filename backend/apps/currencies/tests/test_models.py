from apps.currencies.models import *
from misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)

from django.test import TestCase


class CurrenciesModelTest(TestCase):
    
    def setUpTestData(cls):

        testCurrencyNameUSD = "USD"
        testAbbreviationUSD = "USD"
        testDefaultSystemCurrencyUSD = True

        self.testCurrency = Currency.objects.create(
            name=testCurrencyNameUSD,
            abbreviation=testAbbreviationUSD,
            defaultSystemCurrency=testDefaultSystemCurrencyUSD
        )

    def test_name_label(self):
        currency = currency.objects.get(id=1)
        field_label = currency._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_abbreviaiton_label(self):
        currency = currency.objects.get(id=1)
        field_label = currency._meta.get_field('abbreviation').verbose_name
        self.assertEquals(field_label, 'abbreviation')

    def test_defaultSystemCurrency_label(self):
        currency = currency.objects.get(id=1)
        field_label = currency._meta.get_field('defaultSystemCurrency').verbose_name
        self.assertEquals(field_label, 'defaultSystemCurrency')
