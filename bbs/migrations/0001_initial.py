# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='标题')),
                ('brief', models.CharField(blank=True, max_length=250, null=True, verbose_name='简介')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='发布时间')),
                ('last_modify_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('priority', models.IntegerField(default=1000, verbose_name='优先级')),
                ('status', models.IntegerField(choices=[('draft', '草稿'), ('published', '已发布'), ('hidden', '隐藏')], default='published')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名称')),
                ('brief', models.CharField(blank=True, max_length=250, null=True, verbose_name='分类简介')),
                ('set_as_top_menu', models.BooleanField(default=False, verbose_name='是否是顶部菜单')),
                ('position_index', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_type', models.IntegerField(choices=[(1, '评论'), (2, '点赞')], default=1)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Article', verbose_name='所属文章')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_children', to='bbs.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('signature', models.CharField(blank=True, max_length=250, null=True, verbose_name='标签')),
                ('head_img', models.ImageField(blank=True, height_field=150, null=True, upload_to='', verbose_name='头像', width_field=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.UserProfile'),
        ),
        migrations.AddField(
            model_name='category',
            name='admin',
            field=models.ManyToManyField(blank=True, to='bbs.UserProfile', verbose_name='用户信息'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.UserProfile', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Category', verbose_name='分类'),
        ),
    ]
