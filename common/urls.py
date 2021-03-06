# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from common.apis import UserViewSet, ArticleViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'user', UserViewSet, 'user')
router.register(r'articles', ArticleViewSet, 'articles')

urlpatterns += router.urls
