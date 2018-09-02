# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from common import models


admin.site.register(models.UserExtra)
admin.site.register(models.Article)
