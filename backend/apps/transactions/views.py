import requests
import re
import datetime
import os
import json
import random
import binascii
import PyPDF2
from uuid import uuid4
import io as BytesIO
from base64 import b64decode

from decimal import *
getcontext().prec = 2

from django.db import models
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

from apps.users.models import User
from apps.users.serializers import *

from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.decorators import list_route, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework import filters

from apps.transactions.models import *
from apps.transactions.serializers import *

from apps.transactions.choices import TransactionStatusChoices

from apps.currencies.choices import CURRENCY_TYPE
from apps.currencies.models import Currency, CurrencyRatio

from apps.clients.models import Client, ClientBalance
from apps.misc.logger import *

from django.db.models import Q

logger = logging.getLogger(__name__)
logger.addHandler(handler)


class TransactionsViewSet(viewsets.ModelViewSet):
    parser_classes = (JSONParser,)

    '''
        * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
        * @description 
            Re-writing permissions due to the fact, that we want our user to
            be able to read transactions even if he or she is not logged in
            so that, in such a situation, he or she will see all of the system's transactions
        * @param -
        * @return [list] (transactions)
    '''
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

        return super(TransactionsViewSet, self).get_permissions()

    '''
        * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
        * @description 
            Re-writing this method. Its due to the fact, that
            anonymous user cannot see nicknames of sender and/or recipient.
            He is permitted to only view values / names of currencies 
            in the list of recent transactions 
        * @param -
        * @return - Serializer
    '''

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return TransactionSerializer
        else:
            return TransactionAnonymousSerializer

    '''
        * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
        * @description 
            Returns Client object linked to the
            user, that is currently logged in 
        * @param -
        * @return - queryset
    '''
    def get_user_authenticated(self):
        queriedClient = get_object_or_404(
            Client.objects.all(),
            userObject=self.request.user
        )

        return queriedClient
    '''
        * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
        * @description
         Generates list of transactios processed by the currently logged user
        * @param -
        * @return - queryset
    '''
    def get_queryset(self):

        if self.request.user.is_authenticated:

            queriedClient = self.get_user_authenticated()

            queryset = Transaction.objects.filter(
                Q(
                    recipient=queriedClient
                )
                |
                Q(
                    sender=queriedClient
                )
            )

        else:
            queryset = Transaction.objects.all()

        return queryset

    '''
          * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
          * @description
               
               Functions responsible for transfering money, 
               as well as for converting them.
               There is no need of creating another endpoint - this one is able to handle
               both of these operations
          * @param -
          * @return -
      '''

    @list_route(methods=['POST'])
    def transfer(self, request):

        try:

            fromCurrency = request.data.get('fromCurrency', '')
            toCurrency = request.data.get('toCurrency', '')

            # Formatted as an e-mail address
            toUser = request.data.get('recipient', '')
            transactionValue = request.data.get('value', '')

            if(isinstance(transactionValue, str)):
                transactionValue = transactionValue.strip()



            fromUser =  self.get_user_authenticated()
            # Generating list of currencies ( their abbreviations )
            listOfAcceptableCurrencies = [x[1] for x in CURRENCY_TYPE]
            # Validating input

            if (
                fromCurrency in listOfAcceptableCurrencies
                and
                toCurrency in listOfAcceptableCurrencies
                and
                re.match(
                    r"^[^@]+@[^@]+\.[^@]+$",
                    toUser
                )
                and
                    re.match(
                    r"^\d\d*[.]?\d*$", str(transactionValue)
                )
            ):

                transactionValue =Decimal(
                    transactionValue
                )

                # Querying proper currency objects
                fromCurrency = get_object_or_404(
                    Currency.objects.all(),
                    abbreviation=fromCurrency
                )

                toCurrency=get_object_or_404(
                    Currency.objects.all(),
                    abbreviation=toCurrency
                )

                # Querying to user
                toUser = get_object_or_404(
                    Client.objects.all(),
                    userObject=get_object_or_404(
                        User.objects.all(),
                        email=toUser
                    )
                )

                '''
                Quering balance denoted in the currency
                delivered by the user
                '''

                queriedSenderBalance = ClientBalance.objects.filter(
                    balanceOwner=fromUser,
                    balanceCurrency=fromCurrency
                )

                '''
                    Creating a default 
                    value of transaction ratio
                    In situation in which both of used currencies
                    are the same, it simply is multiplied by 1.0
                    Otherwise, Algorithm uses proper relation
                '''
                transactionRatio = 1.0
                '''
                making sure that from and to currencies 
                are the same
                otherwise we have to convert the value of this transaction
                '''

                if (fromCurrency != toCurrency):
                    '''
                        Fetching the ratio of 
                        parsed currencies
                    '''

                    '''
                    Has to be hard-coded
                    There is a lack of time to
                    do it in a correct way
                    with background process that would fetch the data
                    '''
                    transactionRatio = 1.1

                    # queriedRatio = CurrencyRatio.objects.filter(
                    #     fromCurrency=fromCurrency,
                    #     toCurrency=toCurrency
                    # )
                    #
                    # if(queriedRatio.count() == 1):
                    #     transactionRatio = queriedRatio[0].ratio
                    # else:
                    #     '''
                    #         In order to make the user sure
                    #         that it is the mistake made
                    #         by our platform itself / provider of the
                    #         liquidity
                    #     '''
                    #     return Response(
                    #         status=status.HTTP_406_NOT_ACCEPTABLE
                    #     )

                createdTransaction = Transaction.objects.create(
                    recipient=toUser,
                    sender=fromUser,
                    fromCurrency=fromCurrency,
                    toCurrency=toCurrency,
                    value=transactionValue,
                    exchangeRate=transactionRatio,
                )


                # Determining, whether user has enough funds
                if(
                    queriedSenderBalance[0].balanceValue < transactionValue
                    or transactionValue <= 0
                ):


                    '''
                    Creating transaction object without moving any funds
                    We need this one in order to store
                    the entire history of transactions
                    even these, which could not be realized
                    '''

                    # updating transaction status
                    createdTransaction.transactionStatusChoices = list(filter(lambda x: x[1] == "Failed", TransactionStatusChoices))
                    createdTransaction.save()

                    return Response(
                        status=status.HTTP_409_CONFLICT
                    )

                else:
                    # Updating sender's balance
                    queriedSenderBalance.update(
                        balanceValue = (
                            queriedSenderBalance[0].balanceValue
                            -
                            Decimal(
                                transactionValue
                            )
                        )
                    )

                    # Updating value of the transaction
                    transactionValue *= Decimal(transactionRatio)

                    # Updating recipient's balance
                    queriedRecipientBalance = ClientBalance.objects.filter(
                       balanceOwner=toUser,
                       balanceCurrency=toCurrency
                    )

                    # updating transaction status
                    createdTransaction.transactionStatusChoices = list(
                        filter(lambda x: x[1] == "Processed", TransactionStatusChoices)
                    )
                    createdTransaction.save()

                    queriedRecipientBalance.update(
                        balanceValue=(
                            Decimal(
                                transactionValue
                            ) + queriedRecipientBalance[0].balanceValue
                        )
                    )

                    return Response(
                        status=status.HTTP_200_OK
                    )

        except Exception as e:
            logger.error(
                "Something unexpected happened when in: TransactionsViewSet-transfer:"
                + '\n'
                + str(e)
            )

        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

    '''
          * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
          * @description

               Function responsible for summing up each and every transaction
               that has been created on behalf of given user's nickname
          * @param 
            * [email] (EMAIL) - email of the user. Basing on this field, the transactions will be filtered
            * [datetimefield] (START_DATE) - starting date of the transactions to filter
            * [datetimefield] (END_DATE) - ending date of the transactions to filter
          * @return 
            * [float] (transactions_value) - value of summed transactions
      '''

    @list_route(methods=['GET'])
    def summedtransactions(self, request):

        try:


            userEmailAddress = request.GET.get('EMAIL', '')
            startingDate = datetime.datetime.strptime(
                request.GET.get(
                    'START_DATE',
                    '1990-01-01'
                )[:10],
                "%Y-%m-%d"
            )
            endingDate = datetime.datetime.strptime(
                request.GET.get(
                    'END_DATE',
                    '2999-01-01'
                )[:10],
                "%Y-%m-%d"
            )


            # Querying user
            queriedUser = get_object_or_404(
                Client.objects.all(),
                userObject=get_object_or_404(
                    User.objects.all(),
                    email=userEmailAddress
                )
            )

            # Querying transactions
            queriedTransactions = Transaction.objects.filter(
                Q(recipient=queriedUser)|Q(sender=queriedUser)
            ).filter(
                created_at__range=[startingDate,endingDate]
            )

            '''
                Building up the basic JSON object
                that will be returned
            '''
            jsonDataObject = {
                'total_value': 0.0,
                'number_of_transactions': 0
            }

            if(queriedTransactions.count() > 0):
                # Filling given jsonDataObject with proper data
                for transaction in queriedTransactions:
                    jsonDataObject['total_value'] = jsonDataObject['total_value'] + float(transaction.value)
                    jsonDataObject['number_of_transactions'] = jsonDataObject['number_of_transactions'] + 1

            return Response(
                status=status.HTTP_200_OK,
                data=jsonDataObject
            )

        except Exception as e:
            logger.error(
                "Something unexpected happened when in: TransactionsViewSet-summedtransactions:"
                + '\n'
                + str(e)
            )

        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
