# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers


class JWTUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name')
