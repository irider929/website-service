# -*- coding: utf-8 -*-
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from common.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    """
    user
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            msg = u'用户名已存在'
            return Response({'msg': msg}, status=status.HTTP_400_BAD_REQUEST)
        user = User(username=username)
        user.set_password(password)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        if request.user == user:
            # 修改自己的first_name
            first_name = request.data.get('first_name')
            if first_name:
                user.first_name = first_name
                user.save()
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_403_FORBIDDEN)
