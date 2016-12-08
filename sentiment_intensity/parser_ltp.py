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
import pprint

import xml.etree.ElementTree as Etree

reload(sys)
sys.setdefaultencoding('utf8')


def parser():
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    args = {
        'api_key': 'o9g0E8g50ZtwuZsmfx4A7juNyw0E0M7fic4dgHSK',
        'text': '我非常喜欢苹果。',
        'pattern': 'dp',
        'format': 'xml'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method

    content = result.read().strip(" ")
    print content

    # content_arr = content.split("\n")
    # content = ""
    # for c in content_arr:
    #     temp = c[c.index("<"):c.rindex(">")+1]
    #     # print "--",temp
    #     content = content + temp

    # print chardet.detect(content)
    # print type(content)
    # print content

    root = Etree.fromstring(content)

    sent = root.findall('doc/para/sent/word')
    for s in sent:
        # word = s.find("word")
        # print "[word] ", word.get("cont")
        print "[word] ", s.get("cont")

    print root[1][0][0][0].get("cont")
    print root[1][0][0][1].get("cont")
    print root[1][0][0][2].get("cont")
    print root[1][0][0][3].get("cont")




if __name__ == "__main__":
    parser()

    a = '<?xml version="1.0" encoding="utf-8" ?>' \
        '<xml4nlp>' \
        '<note sent="y" word="y" pos="y" ne="n" parser="y" semparser="n" lstmsemparser="n" wsd="n" srl="n" />' \
        '<doc><para id="0">' \
        '<sent id="0" cont="我非常喜欢苹果。">' \
        '<word id="0" cont="我" pos="r" parent="2" relate="SBV" />' \
        '<word id="1" cont="非常" pos="d" parent="2" relate="ADV" />' \
        '<word id="2" cont="喜欢" pos="v" parent="-1" relate="HED" />' \
        '<word id="3" cont="苹果" pos="n" parent="2" relate="VOB" />' \
        '<word id="4" cont="。" pos="wp" parent="2" relate="WP" />' \
        '</sent></para></doc>' \
        '</xml4nlp>'

    b = '<?xml version="1.0" encoding="UTF-8"?>' \
        '<note><to>World</to>' \
        '<from>Linvo</from>' \
        '<heading>Hi</heading>' \
        '<body>Hello World!</body>' \
        '</note>'

    # root = Etree.fromstring(a)
    # print len(root)
    # print root.find('note')
    # sent = root.findall("note")
    # for s in sent:
    #     word = s.find("to").text()
    #     print word


    # root = Etree.parse("/home/zhangxin/work/workplace_python/stock_industry_sentiment_analysis/sentiment_intensity/text.xml")
    # note = root.find('note')
    # print note.get("sent")