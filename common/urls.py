# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from common.apis import UserViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'users', UserViewSet, 'user')

urlpatterns += router.urls
