import requests
import re
import os
import json
import random
import binascii
import PyPDF2
from uuid import uuid4
import io as BytesIO
from base64 import b64decode

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
# import rest_framework_filters as filters

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

from apps.clients.models import *
from apps.clients.serializers import *
from apps.misc.logger import *

from django.db.models import Q

logger = logging.getLogger(__name__)
logger.addHandler(handler)


class ClientBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = ClientBalanceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser,)

    '''
        * @author name Arthur Drozdzyk <arturdrozdzyk@gmail.com>
        * @description 
            Returns each and every balance wallet linked to the
            user, that is currently logged in
        * @param -
        * @return - queryset
    '''

    def get_queryset(self):

        if self.request.user.is_authenticated:

            queriedClient = get_object_or_404(
                Client.objects.all(),
                userObject=self.request.user
            )

            queryset = ClientBalance.objects.filter(
                balanceOwner=queriedClient
            )

        else:
            queryset = ClientBalance.objects.none()

        return queryset
