# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from common.utils import parse_markdown


class UserExtra(models.Model):
    """
    User模型补充
    """
    user = models.OneToOneField(User, related_name='user_extra')
    follow = models.ManyToManyField(User, verbose_name=u'关注的人', blank=True)

    def __unicode__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(u'标题', max_length=255)
    body_markdown = models.TextField(default='', blank=True)
    body_html = models.TextField(default='', blank=True)
    create_time = models.DateTimeField(u'创建', auto_now_add=True)
    modify_time = models.DateTimeField(u'最后一次修改', auto_now=True)
    author = models.ForeignKey(User, related_name='articles', verbose_name=u'作者')

    def __unicode__(self):
        return self.title

    def update_body_html(self):
        # 在create和update的时候调用
        self.body_html = parse_markdown(self.body_markdown)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body_markdown': self.body_markdown,
            'body_html': self.body_html,
            'create_time': self.create_time.strftime('%Y-%m-%d %X'),
            'modify_time': self.modify_time.strftime('%Y-%m-%d %X'),
            'author': {
                'id': self.author.id,
                'username': self.author.username,
                'first_name': self.author.first_name
            }
        }
