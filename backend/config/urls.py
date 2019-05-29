from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout

from django.conf.urls import include, url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from config.api import api

app_name = 'api'


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),

    url(r'^api/v1/auth/obtain_token/', obtain_jwt_token, name='api-jwt-auth'),
    url(r'^api/v1/auth/verify_token/', verify_jwt_token, name='api-jwt-verify'),
    url(r'^api/v1/auth/refresh_token/', refresh_jwt_token, name='api-jwt-refresh'),  


    path('api/v1/', include((api.urls, 'api')))
]

# Silk: stress testing software
urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
