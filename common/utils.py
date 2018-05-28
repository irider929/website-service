# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name')


def jwt_response_payload_handler(token, user=None, request=None):
    payload = {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
    return payload
