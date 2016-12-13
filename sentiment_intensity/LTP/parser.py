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


def read_dict():
    d_path = "/home/zhangxin/文档/市场情绪分析/文献/依存句法/兰秋军/程度副词_datatang.txt"
    s_path = "/home/zhangxin/文档/市场情绪分析/文献/依存句法/兰秋军/[兰秋军]词典数据.txt"
    n_path = "/home/zhangxin/文档/市场情绪分析/情感词典/刘秒/fou.txt"

    D = {}
    S = {}
    N = []
    P = {}   # 极性词典

    for d in open(d_path):
        temp = d.split(" ")
        word_arr = temp[1].strip("\n").rstrip(" ").split("、")
        for w in word_arr:
            D[w] = temp[0]

    for d in open(s_path):
        d = d.decode("gbk")
        temp = d.split(" ")
        S[temp[0]] = float(temp[1])

        if temp[1] > 0:
            P[temp[0]] = 1
        else:
            P[temp[0]] = -1

    for d in open(n_path):
        N.append(d.strip("\n").replace(" ", "").rstrip().replace("0x20", ""))

    return D, S, N, P


def parser(text, D, N):
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    args = {
        'api_key': 'o9g0E8g50ZtwuZsmfx4A7juNyw0E0M7fic4dgHSK',
        'text': text,
        'pattern': 'dp',
        'format': 'xml'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip(" ")
    # print content

    # 结果解析
    relation_list = []

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
            pos_mw = w.get("pos")
            pos_cw = cword.get("pos")
            id_mw = w.get("id")
            id_cw = cword.get("id")
            dd_mw = False
            dd_cw = False
            nd_mw = False
            nd_cw = False

            # 判断是否程度副词
            if pos_mw == "d" and D.has_key(mw):
                dd_mw = True

            if pos_cw == "d" and D.has_key(cw):
                dd_cw = True

            # 判断是否否定词
            if pos_mw == "d" and N.__contains__(mw):
                nd_mw = True

            if pos_cw == "d" and N.__contains__(cw):
                nd_cw = True

            print mw, cw, relate, pos_mw, pos_cw, id_mw, id_cw, dd_mw, dd_cw, nd_mw, nd_cw, "\n"

            add_relation = relation.Relation(mw, cw, relate, pos_mw, pos_cw, id_mw, id_cw, dd_mw, dd_cw, nd_mw, nd_cw)
            relation_list.append(add_relation)

    # try:

    # except Exception:
    #     print '异常',Exception

    return relation_list


if __name__ == "__main__":

    D, S, N, P = read_dict()
    N.append(u"不")
    D[u"非常"] = 99
    # for d in D.keys():
        # print d, D[d]

    # 单句测试
    text = "我喜欢苹果,但是讨厌小米"
    text4 = "我非常不喜欢苹果"
    text5 = "亏损幅度很大"
    result = parser(text, D, N)
    score_all = 0
    for r in result:
        print r.mw, " - ", r.relation, " - ", r.cw
        temp = score.score(r, D, S, P)
        score_all += temp
        print temp
        print "\n\n"

    print "[总情感值] ", score_all


    # 测试基于依存句法的二叉树
    # binary_tree.btree_xrc(result, [u"我",u"非常",u"不",u"喜欢",u"苹果"])
    binary_tree.btree_zx(result)
