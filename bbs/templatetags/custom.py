#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import template
from django.utils.html import format_html


register = template.Library()


@register.simple_tag
def filter_comment(article_obj):
    query_set = article_obj.comment_set.select_related()
    comments = {
        'comment_count': query_set.filter(comment_type=1).count(),
        'thumb_count': query_set.filter(comment_type=2).count(),
    }
    return comments
