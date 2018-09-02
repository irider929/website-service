# -*- coding: utf-8 -*-
import markdown

from common.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user).data
    }


def parse_markdown(text):
    html = markdown.markdown(
        text,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite'
        ],
        output_format='html5'
    )
    return html
