# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # 避免序列化重要的信息
        fields = ('id', 'username', 'first_name', 'email')
