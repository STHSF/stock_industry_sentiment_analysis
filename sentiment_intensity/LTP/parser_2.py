#!/usr/bin/env python
# encoding: utf-8
# -*- coding:utf8 -*-

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: parser_ltp.py
# Time: 16-12-7 下午5:38
# -------------------------------------------
import sys
import urllib, urllib2
import xml.etree.ElementTree as Etree
import time
import score
import relation
import binary_tree

reload(sys)
sys.setdefaultencoding('utf-8')


def parser(text):
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    args = {
        'api_key': 'o9g0E8g50ZtwuZsmfx4A7juNyw0E0M7fic4dgHSK',
        'text': text,
        'pattern': 'dp',
        'format': 'xml'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip(" ")
    print content

    # 结果解析
    relation_list = []

    root = Etree.fromstring(content)
    print type(root)
    root.draw()
    # word = root.findall('doc/para/sent/word')


if __name__ == '__main__':

    # 单句测试
    text = "我喜欢苹果,但是讨厌小米"
    # text4 = "我非常不喜欢苹果"
    # text5 = "亏损幅度很大"
    result = parser(text)
