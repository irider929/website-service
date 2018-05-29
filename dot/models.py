# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Dot(models.Model):
    content = models.TextField()
    author = models.ForeignKey(to=User)

    def __unicode__(self):
        return self.content[:10]
