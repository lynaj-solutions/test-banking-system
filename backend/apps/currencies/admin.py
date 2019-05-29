from django.contrib import admin
from apps.currencies.models import *

admin.site.register(Currency)
admin.site.register(CurrencyRatio)
