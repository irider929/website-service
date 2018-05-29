# -*- coding: utf-8 -*-
from common.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    payload = {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
    return payload
