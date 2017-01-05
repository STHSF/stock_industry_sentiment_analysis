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

pos_dict = []
neg_dict = []
fou_dict = []     # 否定词


def init():
    global pos_dict
    global neg_dict
    global fou_dict
    path = '/home/zhangxin/文档/市场情绪分析/情感词典/stanford'

    # 读取词典
    s_path = path + "/senti.txt"
    f_path = path + "/fou.txt"

    # 结巴新词
    word_add = set()

    for s in open(s_path):
        temp = s.decode("utf-8").split(" ")
        word_add.add(temp[0])
        if float(temp[1]) > 0:
            pos_dict.append(temp[0])
        else:
            neg_dict.append(temp[0])

    for f in open(f_path):
        f = f.decode("utf-8-sig")
        fou_dict.append(f.strip("\n"))
        word_add.add(f.strip("\n"))

    jieba.add_word("瓜达尔")
    for w in word_add:
        jieba.add_word(w)
