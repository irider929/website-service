# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from dot import views


router = DefaultRouter()
router.register(r'dot', views.DotViewSet, base_name='dot')

urlpatterns = [
]

urlpatterns += router.urls
