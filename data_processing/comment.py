#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能： 评论模块
# Author: zx
# Software: PyCharm Community Edition
# File: comment.py
# Time: 16-11-24 上午10:48
# -------------------------------------------

class Comment:
    def __init__(self, id, content, reply, title, time, stock):
        self.id = id
        self.content = content
        self.reply = reply
        self.title = title
        self.time = time
        self.stock = stock

    @property
    def get_id(self):
        return self.id

    @property
    def get_content(self):
        return self.content

    @property
    def get_reply(self):
        return self.reply

    @property
    def get_title(self):
        return self.title

    @property
    def get_time(self):
        return self.time

    @property
    def get_stock(self):
        return self.stock
