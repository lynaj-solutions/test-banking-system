from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from apps.misc.logger import *
from apps.currencies.choices import *

# +++++++++++++++++++++++++++++++++++
logger = logging.getLogger(__name__)
logger.addHandler(handler)
# +++++++++++++++++++++++++++++++++++


class Currency(models.Model):
    name = models.CharField(
        choices=CURRENCY_TYPE,
        default=next(iter(CURRENCY_TYPE))[0],
        max_length=300,
        null=False,
        verbose_name='Name of the currency'
    )

    abbreviation = models.CharField(
        default="",
        max_length=30,
        null=False,
        verbose_name='Abbreviation of the currency'
    )

    defaultSystemCurrency = models.BooleanField(
        default=False,
        verbose_name='Is a default currency of the entire system'
    )

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return '%s' % (self.name)

class CurrencyRatio(models.Model):
    fromCurrency = models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='First currency of the relation',
        related_name="currency_ratio_from_currency"
    )

    toCurrency = models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Second currency of the relation',
        related_name="currency_ratio_to_currency"
    )

    ratio = models.DecimalField(
        default=0.0,
        max_digits=190,
        null=True,
        decimal_places=4,
        verbose_name='Ratio of linked currencies'
    )





# # Making sure that there is only one
# # default currency of the entire platform
# def SecurePlatformOnlyOneDefaultCurrencyAllowed(sender,
#     instance,
#     created,
#     raw,
#     using,
#     update_fields,
#     **kwargs):
#         try:
#             '''
#             If currently operated intance
#             is defined as a default currency
#             of this system,
#             we have to set this field as "False" for each and every other currency
#             '''
#             if(
#                 not created and
#                 instance.defaultSystemCurrency == True
#             ):
#                 # Creating a BULK opreration
#                 Currency.objects.all().exclude(id=instance.id).update(
#                     defaultSystemCurrency=False
#                 )

#             instance.save()

#         except Exception as e:
#             logger.error(
#                 '[*** TRIGGER ***] [ ERROR ] [ CreateCompany ]'
#                 +
#                 'Problem: exception occured during the process of creating Company object and linking it to the newly create Owner account'
#                 + 'error: ' + str(e)
#             )



# # post_save.connect(SecurePlatformOnlyOneDefaultCurrencyAllowed, sender=Currency)
