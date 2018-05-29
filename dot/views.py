# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.response import Response

from dot.models import Dot
from dot.serializers import DotSerializer


class DotViewSet(viewsets.ViewSet):
    def list(self, request):
        dot_queryset = Dot.objects.all()
        dot_serialized = DotSerializer(dot_queryset, many=True).data
        return Response(dot_serialized)
