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

deg_dict = {}
senti_dict = {}
eng_dict = {}
fou_dict = []
but_dict = []


def dict():
    # 读取词典
    d_path = "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/程度副词_datatang.txt"
    s_path = "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/senti.txt"
    f_path = "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/fou.txt"
    b_path = "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/but.txt"
    e_path = "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/eng.txt"

    path_dic = {
        'd_path': "/Users/li/workshop/MyRepository/stock_industry_sentiment_analysis/"
                  "data_warehouse/stanford/jars/stanford/程度副词_datatang.txt",
        's_path': "/Users/li/workshop/MyRepository/stock_industry_sentiment_analysis/"
                  "data_warehouse/stanford/jars/stanford/[兰秋军]词典数据.txt",
        'f_path': "/Users/li/workshop/MyRepository/stock_industry_sentiment_analysis/"
                  "data_warehouse/stanford/jars/stanford/fou.txt",
        'b_path': "/Users/li/workshop/MyRepository/stock_industry_sentiment_analysis/"
                  "data_warehouse/stanford/jars/stanford/but.txt"
    }

    for d in open(d_path):
        temp = d.decode("utf-8").split(" ")
        word_arr = temp[1].strip("\n").rstrip(" ").split("、")
        for w in word_arr:
            deg_dict[w] = temp[0]

    for s in open(s_path):
        temp = s.decode("utf-8").split("\t")
        senti_dict[temp[0]] = float(temp[1])

    for f in open(f_path):
        f = f.decode("utf-8-sig")
        fou_dict.append(f.strip("\n"))

    for b in open(b_path):
        but_dict.append(b.strip("\n"))

    for e in open(e_path):
        temp = e.split(" ")
        eng_dict[temp[0]] = float(temp[1])

    # 结巴添加新词
    jieba.add_word(unicode("淡定"))
    jieba.add_word(unicode("非公开"))
    jieba.add_word(unicode("审核通过"))
    jieba.add_word(unicode("加仓"))
    jieba.add_word(unicode("没潜力"))
    jieba.add_word(unicode("没动力"))
    jieba.add_word(unicode("肿么了"))
    jieba.add_word(unicode("创新低"))
    jieba.add_word(unicode("不成人形"))
