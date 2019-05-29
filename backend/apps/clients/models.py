from uuid import uuid4

from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import uuid

from apps.users.models import User
from apps.currencies.models import Currency
from apps.misc.logger import *

import environ

env = environ.Env()

# +++++++++++++++++++++++++++++++++++
logger = logging.getLogger(__name__)
logger.addHandler(handler)
# +++++++++++++++++++++++++++++++++++


class Client(models.Model):
    userObject = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Linked user object'
    )

    nativeAccountCurrency= models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Linked currency'
    )

    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=timezone.now
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        blank=True,
        auto_now_add=timezone.now
    )



class ClientBalance(models.Model):
    balanceOwner = models.ForeignKey(
        Client,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Linked Client object'
    )

    balanceCurrency = models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Linked currency'
    )

    balanceValue = models.DecimalField(
        default=0.0,
        max_digits=190,
        null=True,
        decimal_places=4,
        verbose_name='Value of the balance'
    )

    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=timezone.now
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        blank=True,
        auto_now_add=timezone.now
    )


'''
    * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
    * @description 
        The method is creating ClientBalance for each and every available currency
        & linking it with corresponded Client account
    * @param -
    * @return -
'''


def CreateBasicCurrencyStack(sender,
                        instance,
                        **kwargs):
    try:
        # Making sure there exist at least one currency in the system
        queriedCurrencies = Currency.objects.all()
        if(queriedCurrencies.count() == 0):
            Currency.objects.create(name="USD", abbreviation="USD", defaultSystemCurrency=True)
            Currency.objects.create(name="GBP", abbreviation="GBP", defaultSystemCurrency=False)
            Currency.objects.create(name="EURO", abbreviation="EURO", defaultSystemCurrency=False)

    except Exception as e:
        logger.error(
            '[*** TRIGGER ***] [ ERROR ] [ CreateBasicCurrencyStack ] '
            +
            'Problem: exception occured during the process of creating basic Currencies objects'
            + 'error: ' + str(e)
        )

def LinkBasicCurrencyStack(sender,
                        instance,
                        created,
                        raw,
                        using,
                        update_fields,
                        **kwargs):
    if created:

        try:

            for currency in Currency.objects.all():
                '''
                    determining with given currency is a default
                    one or not
                    If so, it's value should equal hard-coded value
                '''
                balanceValue = 0

                if(currency.defaultSystemCurrency):
                    balanceValue = 1000
                        # env.bool('DEFAULT_CURRENCY_VALUE')

                ClientBalance.objects.create(
                    balanceOwner=instance,
                    balanceCurrency=currency,
                    balanceValue=balanceValue
                )

        except Exception as e:
            logger.error(
                '[*** TRIGGER ***] [ ERROR ] [ LinkBasicCurrencyStack ] '
                +
                'Problem: exception occured during the process of creating ClientBalance'
                + 'error: ' + str(e)
            )


'''
    * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
    * @description 
        The method is creating Client object
        & linking it with corresponded User obj
    * @param -
    * @return -
'''

def CreateBasicClientObject(sender,
                        instance,
                        created,
                        raw,
                        using,
                        update_fields,
                        **kwargs):
    if created:

        try:

            queriedNativeSystemCurrency = Currency.objects.filter(
                defaultSystemCurrency=True
            )
            if(queriedNativeSystemCurrency.count() >= 1):
                Client.objects.create(
                    userObject=instance,
                    nativeAccountCurrency=queriedNativeSystemCurrency[0]
                )
            else:
                raise Exception("Default currency of the system is not valid.")


        except Exception as e:
            logger.error(
                '[*** TRIGGER ***] [ ERROR ] [ CreateBasicClientObject ] '
                +
                'Problem: exception occured during the process of creating ClientBalance'
                + 'error: ' + str(e)
            )

'''
    * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
    * @description 
        Handles the deletion of linked Client object, linked to the User object, that is being deleted
    * @param -
    * @return -
'''
def SafeDeletionOfTheClientObject(sender, instance, **kwargs):

    try:

        queriedClient = Client.objects.filter(
            userObject=instance
        )

        if(queriedClient.count() > 0):
            queriedClient.delete()

    except Exception as e:
        logger.error(
			'Problem: error happened when in safe_deletion_of_the_image'
			+ '\nerror: ' + str(e)
		)


'''
    * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
    * @description 
        Handles the deletion of linked ClientBalance object, linked to the Client object, that is being deleted
    * @param -
    * @return -
'''
def SafeDeletionOfTheClientBalanceObject(sender, instance, **kwargs):

    try:

        queriedBalance = ClientBalance.objects.filter(
            balanceOwner=instance
        )

        if(queriedBalance.count() > 0):
            queriedBalance.delete()

    except Exception as e:
        logger.error(
			'Problem: error happened when in safe_deletion_of_the_image'
			+ '\nerror: ' + str(e)
		)

post_save.connect(LinkBasicCurrencyStack, sender=Client)
pre_save.connect(CreateBasicCurrencyStack, sender=User)
post_save.connect(CreateBasicClientObject, sender=User)

pre_delete.connect(SafeDeletionOfTheClientObject, sender=User)
pre_delete.connect(SafeDeletionOfTheClientBalanceObject, sender=Client)
