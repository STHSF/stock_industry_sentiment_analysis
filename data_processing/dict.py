#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: dict.py
# Time: 16-12-1 下午3:18
# -------------------------------------------
import os


# 处理字典
def get_dict():
    liu = "/home/zhangxin/文档/市场情绪分析/情感词典/刘秒"
    zhi = "/home/zhangxin/文档/市场情绪分析/情感词典/知网"
    li = "/home/zhangxin/文档/市场情绪分析/情感词典/李煜"

    zhi_pos = []
    zhi_neg = []

    zhi_list = os.listdir(zhi)
    for f in zhi_list:
        print "[", f, "]"

        if f.__contains__("neg"):
            for d in open(zhi + "/" + f, "r"):
                zhi_neg.append(d.strip('\n'))

        if f.__contains__("pos"):
            for d in open(zhi + "/" + f, "r"):
                zhi_pos.append(d.strip('\n'))

    return zhi_pos, zhi_neg


# 处理程度副词
def get_dict_deg():
    adeg = "/home/zhangxin/文档/市场情绪分析/情感词典/adeg.dict"
    data = open(adeg)
    deg_map = {}
    label = ""
    for d in data:
        d = d.strip("\n")
        # d = d.strip().replace(" ","").replace("\t","")
        # print len(d), "-", d, "-"
        if d.__contains__("#"):
            label = d[d.index("#") + 1:d.rindex("#")]
        else:
            deg_map[unicode(d)] = label

    return deg_map