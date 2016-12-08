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

reload(sys)
sys.setdefaultencoding('utf8')


# 依存关系类
class Relation:
    def __init__(self, mw, cw, relation, pos_mw, pos_cw, id_mw, id_cw):
        self.mw = mw  # 修饰词
        self.cw = cw  # 支配词
        self.relation = relation
        self.pos_mw = pos_mw
        self.pos_cw = pos_cw
        self.id_mw = id_mw
        self.id_cw = id_cw


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

    # 结果解析
    relation_list = []

    try:
        root = Etree.fromstring(content)

        word = root.findall('doc/para/sent/word')

        # 抽取6种依存关系:ADV, ATT, COO, SBV, VOB, CMP
        relates = ["ADV", "ATT", "COO", "SBV", "VOB", "CMP"]

        for w in word:

            relate = w.get("relate")
            if relates.__contains__(relate):
                cword = word[int(w.get("parent"))]
                mw = w.get("cont")  # 修饰词
                cw = cword.get("cont")  # 支配词
                relation = relate
                pos_mw = w.get("pos")
                pos_cw = cword.get("cont")
                id_mw = w.get("id")
                id_cw = cword.get("id")
                relation = Relation(mw, cw, relation, pos_mw, pos_cw, id_mw, id_cw)
                relation_list.append(relation)
    except Exception:
        print '异常'

    return relation_list


if __name__ == "__main__":

    # 单句测试
    # text = "我喜欢苹果,讨厌小米"
    text_0 = "我喜欢苹果,讨厌小米"
    result = parser(text_0)
    for r in result:
        print r.mw, " - ", r.relation, " - ", r.cw

    # 耗时测试
    # time_begin = time.time()
    # text = "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族." \
    #        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族." \
    #        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族." \
    #        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
    #        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
    #        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
    #        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
    #        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
    #        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族"
    # text_arr = text.split(".")
    # result_list = []
    # count = 1
    # for t in text_arr:
    #     print count, " ", t
    #     count += 1
    #     result = parser(t)
    #     result_list.append(result)
    #
    # time_end = time.time()
    # print "[句子个数] ", len(text_arr)
    # print "[结果] ", len(result_list)
    # print "[总耗时]", time_end - time_begin
