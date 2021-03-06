#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url, include

from bbs import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^category/(\d+)/$', views.category),
    url(r'^detail/(\d+)/$', views.article_detail, name="article_detail"),
    url(r'^comment/$', views.comment, name="post_comment"),
    url(r'^comment/(\d+)/$', views.get_comments, name="get_comments"),

    url(r'^new-article/$', views.new_articles, name="new-article"),
    url(r'^latest_article_count/$', views.get_latest_article_count, name="get_latest_article_count"),


]


