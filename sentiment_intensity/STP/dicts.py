#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：词典加载，结巴添加新词
# Author: zx
# Software: PyCharm Community Edition
# File: dict.py
# Time: 16-12-14 下午5:20
# -------------------------------------------
import jieba

deg_dict = {}     # 程度副词
senti_dict = {}   # 情感词
eng_dict = {}     # 英语或拼音词
fou_dict = []     # 否定词
but_dict = []     # 转折词
lim_dict = []     # 限定词


def init():
    path = '/Users/li/workshop/StanfordNLP/stanfordcorpus'
    # path = '/home/zhangxin/文档/市场情绪分析/情感词典/stanford'

    # 读取词典
    d_path = path + "/程度副词_datatang.txt"
    s_path = path + "/senti.txt"
    f_path = path + "/fou.txt"
    b_path = path + "/but.txt"
    e_path = path + "/eng.txt"
    l_path = path + "/limit.dict"

    # 结巴新词
    word_add = set()

    for d in open(d_path):
        temp = d.decode("utf-8").split(" ")
        word_arr = temp[1].strip("\n").rstrip(" ").split("、")
        for w in word_arr:
            deg_dict[w] = float(temp[0])
            word_add.add(temp[0])

    for s in open(s_path):
        temp = s.decode("utf-8").split(" ")
        senti_dict[temp[0]] = float(temp[1])
        word_add.add(temp[0])

    for e in open(e_path):
        temp = e.split(" ")
        eng_dict[temp[0]] = float(temp[1])
        word_add.add(temp[0])

    for f in open(f_path):
        f = f.decode("utf-8-sig")
        fou_dict.append(f.strip("\n"))
        word_add.add(f.strip("\n"))

    for b in open(b_path):
        but_dict.append(b.strip("\n"))
        word_add.add(b.strip("\n"))

    for l in open(l_path):
        lim_dict.append(l.strip("\n"))
        word_add.add(l.strip("\n"))

    # 结巴添加新词
    jieba.add_word(unicode("淡定"))
    jieba.add_word(unicode("非公开"))
    jieba.add_word(unicode("不成人形"))

    for w in word_add:
        jieba.add_word(w)
