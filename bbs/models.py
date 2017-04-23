from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import datetime
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name=u"标题")
    brief = models.CharField(null=True, blank=True, max_length=250, verbose_name=u"简介")
    category = models.ForeignKey("Category", verbose_name=u"分类")
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile", verbose_name=u"作者")
    pub_date = models.DateTimeField(verbose_name=u"发布时间", blank=True, null=True)
    last_modify_date = models.DateTimeField(verbose_name=u"修改时间", auto_now=True)
    priority = models.IntegerField(verbose_name=u"优先级", default=1000)
    head_img = models.ImageField(verbose_name=u"文章标题图片", upload_to="article/%Y/%m/")
    status_choices = (("draft", u"草稿"),
                      ("published", u"已发布"),
                      ("hidden", u"隐藏"))
    status = models.CharField(choices=status_choices, default="published", max_length=50, verbose_name=u"状态")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = u"文章"

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(_('Draft entries may not have a publication date.'))
        # Set the pub_date for published items if it hasn't been set already.
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name=u"所属文章")
    parent_comment = models.ForeignKey('self', related_name="my_children", blank=True, null=True)
    comment_choices = ((1, u"评论"),
                       (2, u"点赞"))
    comment_type = models.IntegerField(choices=comment_choices, default=1)
    user = models.ForeignKey("UserProfile")
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.comment_type == 1 and len(self.comment) == 0:
            raise ValidationError(u"评论不能为空!")

    def __str__(self):
        return "%s, P:%s, %s" % (self.article, self.parent_comment, self.comment)

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = u"评论"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"分类名称")
    brief = models.CharField(null=True, blank=True, max_length=250, verbose_name=u"分类简介")
    set_as_top_menu = models.BooleanField(default=False, verbose_name="是否是顶部菜单")
    position_index = models.SmallIntegerField(verbose_name=u"顶部排列位置")
    admin = models.ManyToManyField("UserProfile", blank=True, verbose_name=u"用户信息")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = u"分类"


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=u"用户")
    name = models.CharField(max_length=32, verbose_name=u"名称")
    signature = models.CharField(max_length=250, blank=True, null=True, verbose_name=u"标签")
    head_img = models.ImageField(height_field=150, width_field=150, blank=True, null=True, verbose_name=u"头像")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = u"用户"

