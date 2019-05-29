import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

import json
import os
import codecs

from apps.currencies.models import *
from apps.users.models import *
from apps.transactions.models import *
from apps.clients.models import *

from apps.currencies.choices import CURRENCY_TYPE

from misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)


class CompanyViewSetTestCase(APITestCase):
    url = reverse('api:balances-list')

    def setUp(self):
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

        self.queriedCurrencies = Currency.objects.all()

        '''
            Making sure that number of created currencies
            matches these stored in choices.py
            '''
        self.assertEqual(
            self.queriedCurrencies.count(),
            len(CURRENCY_TYPE)
        )

        '''
        Creating & setting up test users
        as well as logging in & receiving a JWT token
        '''
        test_first_name__first_user = "Karl"
        test_last_name__first_user = "Mark"

        test_email__first_user= "johnymarge1@wp.pl"

        test_password__first_user = "ij43i$#@"

        url = reverse('api-jwt-auth')

        self.test_first_user = User.objects.create_user(
            first_name=test_first_name__first_user,
            last_name=test_last_name__first_user,
            email=test_email__first_user,
            password=test_password__first_user
        )

        self.test_first_user.is_active = False
        self.test_first_user.save()

        resp = self.client.post(url, {'email': test_email__first_user, 'password': test_password__first_user}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        self.test_first_user.is_active = True
        self.test_first_user.save()

        self.token = ''

        resp = self.client.post(url, {'email': test_email__first_user, 'password': test_password__first_user}, format='json')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        self.token = resp.data['token']

        # Validating that Client object has been created & linked to the User obj
        self.test_first_user_client_object = Client.objects.filter(
            userObject=self.test_first_user
        )


        self.assertEqual(self.test_first_user_client_object.count(), 1)
        verification_url = reverse('api-jwt-verify')

        resp = self.client.post(verification_url, {'token': self.token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        self.client = APIClient()

    # def TTtest_multiple_balances_default_values(self):
    #     transferValue = 1000.0
    #     test_ratio = 1.1
    #
    #     # Making sure user has enough funds
    #     queriedSenderBalance = ClientBalance.objects.filter(
    #         balanceOwner=self.test_first_user_client_object[0],
    #         balanceCurrency=self.queriedCurrencies[0]
    #     )
    #
    #     queriedSenderBalance.update(
    #         balanceValue=transferValue
    #     )
    #     logger.error('self.queriedCurrencies[1]: ' + str(self.queriedCurrencies[1]))
    #     # Creating a request
    #     test_payload = {
    #         "fromCurrency": self.queriedCurrencies[0].abbreviation,
    #         "toCurrency": self.queriedCurrencies[1].abbreviation,
    #         "toUser": self.test_first_user.email,
    #         "transactionValue": transferValue
    #     }
    #
    #     response = self.client.post(
    #         self.url,
    #         data=test_payload,
    #         format='json',
    #         HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
    #     )
    #
    #     '''
    #     There should be exactly three
    #     wallets returned
    #     '''
    #
    #     logger.error('response: ' + str(response))
    #     logger.error('response data: ' + str(response.data))
    #
    #
    #     self.assertEqual(response.status_code, 200)
    #
    #     # Refreshing querysets
    #     queriedSenderBalance[0].refresh_from_db()
    #
    #     # Making sure that the transfer took a place
    #     self.assertEqual(
    #         queriedSenderBalance[0].balanceValue,
    #         0.0
    #     )
    #
    # def TTtest_multiple_balances_changed_values(self):
    #     transferValue = 1000.0
    #     test_ratio = 1.1
    #
    #     # Making sure user has enough funds
    #     queriedSenderBalance = ClientBalance.objects.filter(
    #         balanceOwner=self.test_first_user_client_object[0],
    #         balanceCurrency=self.queriedCurrencies[0]
    #     )
    #
    #     queriedSenderBalance.update(
    #         balanceValue=transferValue
    #     )
    #
    #     # Creating a request
    #     test_payload = {
    #         "fromCurrency": self.queriedCurrencies[0].abbreviation,
    #         "toCurrency": self.queriedCurrencies[0].abbreviation,
    #         "toUser": self.test_first_user.email,
    #         "transactionValue": transferValue
    #     }
    #
    #     response = self.client.post(
    #         self.url,
    #         data=test_payload,
    #         format='json',
    #         HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
    #     )
    #
    #     self.assertEqual(response.status_code, 200)
    #
    #     # Refreshing querysets
    #     queriedSenderBalance[0].refresh_from_db()
    #
    #     # Making sure that the transfer took a place
    #     self.assertEqual(
    #         queriedSenderBalance[0].balanceValue,
    #         0.0
    #     )
