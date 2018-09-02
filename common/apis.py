# -*- coding: utf-8 -*-
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from common.models import UserExtra, Article
from common.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_user_extra_or_create(user):
        if not isinstance(user, User):
            raise ValueError(u'param must be User type')
        try:
            user_extra = UserExtra.objects.get(user=user)
        except UserExtra.DoesNotExist:
            user_extra = UserExtra.objects.create(user=user)
        return user_extra

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        # 后面移除这个方法
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
            first_name = request.data.get('first_name')
            password = request.data.get('password')
            if first_name:
                user.first_name = first_name
            if password:
                user.set_password(password)
            user.save()
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_403_FORBIDDEN)

    @action(methods=['GET'], detail=False)
    def my_follow(self, request):
        user_extra = self.get_user_extra_or_create(request.user)
        serializer = UserSerializer(user_extra.follow.all(), many=True)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, id=pk)
        return Response(article.serialize())

    def list(self, request):
        articles = Article.objects.all()
        return Response([item.serialize() for item in articles])

    def create(self, request):
        if not request.auth:
            return Response({}, status=status.HTTP_403_FORBIDDEN)
        title = request.data.get('title')
        body = request.data.get('body')
        if title and body:
            article = Article.objects.create(title=title, body=body, author=request.user)
            return Response(article.serialize(), status=status.HTTP_201_CREATED)
        else:
            data = {'detail': u'title和body字段都为必填项'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
