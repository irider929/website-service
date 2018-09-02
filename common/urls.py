# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from common.apis import UserViewSet, ArticleViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'user', UserViewSet, 'user')
router.register(r'article', ArticleViewSet, 'article')

urlpatterns += router.urls
