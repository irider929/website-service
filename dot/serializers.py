# -*- coding: utf-8 -*-
from rest_framework import serializers

from dot import models
from common.serializers import UserSerializer


class DotSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = models.Dot
        fields = (
            'content', 'author'
        )
