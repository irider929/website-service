# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
]
