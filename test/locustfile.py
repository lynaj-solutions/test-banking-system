from locust import HttpLocust, TaskSet, task
from random import randrange
import json

class UserBehavior(TaskSet):
    # tasks = {index: 2, balance: 1}

    randomizedField = str(
        randrange(1000000000)
    ) + "am@wp.pl"
    token = ''
    number_of_transaction = 1000000

    # def on_start(self):
    #     '''
    #         Creating default currencies
    #         Due to the existence of Trigger locked on Client object,
    #         this operation has to be completed before
    #         the creation of the user
    #     '''

    #     currencyIterator = iter(CURRENCY_TYPE)
    #     for currencies in range(len(CURRENCY_TYPE)):
    #         nextCurrency = next(currencyIterator)
    #         if (currencies == 0):
    #             Currency.objects.create(
    #                 name=nextCurrency[0],
    #                 abbreviation=nextCurrency[1],
    #                 defaultSystemCurrency=True
    #             )
    #         else:
    #             Currency.objects.create(
    #                 name=nextCurrency[0],
    #                 abbreviation=nextCurrency[1]
    #             )

    #     self.queriedCurrencies = Currency.objects.all()

    #     '''
    #         Making sure that number of created currencies
    #         matches these stored in choices.py
    #         '''
    #     self.assertEqual(
    #         self.queriedCurrencies.count(),
    #         len(CURRENCY_TYPE)
    #     )

    #     '''
    #         Creating a test user
    #         and linking it with a massive amount of transactions
    #         so that it will allow us to determine
    #         the server's reaction on requests filled with multiple queries
    #     '''
    #     test_first_name__first_user = "Karl"
    #     test_last_name__first_user = "Mark"

    #     test_email__first_user= "johnymarge1@wp.pl"

    #     test_password__first_user = "ij43i$#@"


    #     self.test_first_user = User.objects.create_user(
    #         first_name=test_first_name__first_user,
    #         last_name=test_last_name__first_user,
    #         email=test_email__first_user,
    #         password=test_password__first_user
    #     )

    #     self.test_first_user.is_active = False
    #     self.test_first_user.save()

    #     queriedClient = Client.objects.all()[0]

    #     # Creating dummy transactions
    #     for x in range(self.number_of_transaction):
    #         Transaction.objects.create(
    #             recipient=queriedClient,
    #             sender=queriedClient,
    #             fromCurrency=self.queriedCurrencies[0],
    #             toCurrency=self.queriedCurrencies[0],
    #             value=1
    #         )

    #     '''
    #         Making sure, that the number of transactions equals
    #         planned one
    #     '''
    #     if(Transaction.objects.all().count() != self.number_of_transaction):
    #         raise Exception('WRONG NUMBER OF TRANSACTIONS')


    # def on_stop(self):
    #     # Cleaning up created transactions & test user
    #     Transaction.objects.filter(
    #         Q(
    #             recipient=self.test_first_user
    #         )
    #         ||
    #         Q(
    #             sender=self.test_first_user
    #         )
    #     ).delete()

    #     self.test_first_user.delete()

    @task(1)
    def computational_function_invoke(l):
        auth_response = l.client.get("/api/v1/transactions/summedtransactions/?EMAIL=test@test.test")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

