#!/usr/bin/env python
# -*- coding: utf-8 -*-


def add_node(tree_dic, comment):
    if comment.parent_comment is None:
        # 没有父级
        tree_dic[comment] = {}
    else:
        # 有父级
        for k, v in tree_dic.items():
            if k == comment.parent_comment:
                # 找到你爸
                tree_dic[comment.parent_comment][comment] = {}
            else:
                # 进入下一次继续找
                add_node(v, comment)


def render_tree_node(tree_dic, margin_val):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='comment-node' style='margin-left:%spx'>" % margin_val + k.comment + "<span style='margin-left:20px'>%s</span>" % k.date\
              + "<span style='margin-left:20px'>%s</span>" % k.user.name \
              + '<span comment-id="%s"' % k.id + ' style="margin-left:20px" class="glyphicon glyphicon-comment add-comment" aria-hidden="true"></span>'\
        +  "</div>"
        html += ele
        html += render_tree_node(v, margin_val + 10)
    return html


def render_comment_tree(tree_dic):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='root-comment'>" + k.comment + "<span style='margin-left:20px'>%s</span>" % k.date\
              + "<span style='margin-left:20px'>%s</span>" % k.user.name\
              + '<span comment-id="%s"' % k.id + ' style="margin-left:20px" class="glyphicon glyphicon-comment add-comment" aria-hidden="true"></span>'\
              + "</div>"
        html += ele
        html += render_tree_node(v, 10)
    return html


def build_tree(comment_set):
    # print(comment_set)
    tree_dic = {}
    for comment in comment_set:
        add_node(tree_dic, comment)

    return tree_dic

