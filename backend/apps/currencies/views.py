import requests
from uuid import uuid4

from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from apps.currencies.models import *
from apps.currencies.serializers import *

from apps.misc.logger import *

logger = logging.getLogger(__name__)
logger.addHandler(handler)

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = []