#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url, include

from bbs import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^category/(\d+)/$', views.category),


]


