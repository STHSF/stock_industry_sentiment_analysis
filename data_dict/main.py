#!/usr/bin/env python
# encoding: utf-8
# -*- coding:utf-8 -*-
# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 16-11-29 下午7:24
# -------------------------------------------
import os
import data_processing.read_data as read_data

# 处理字典
def run():
    liu = "/home/zhangxin/文档/市场情绪分析/情感词典/刘秒"
    zhi = "/home/zhangxin/文档/市场情绪分析/情感词典/知网"
    li = "/home/zhangxin/文档/市场情绪分析/情感词典/李煜"

    apos = []
    aneg = []

    zhi_list = os.listdir(zhi)
    for f in zhi_list:
        print "[", f, "]"
        data = open(zhi + "/" + f)
        for d in data:
            print d


# 处理案例句
def process():
    data_path = "/home/zhangxin/文档/市场情绪分析/SH600537_2"
    data_path_2 = "/home/zhangxin/文档/市场情绪分析/SH600537_4"

    wr = open(data_path_2, "wb")
    count = 1

    dlong = []
    for d in open(data_path):
        n = d.rfind("]")

        if n == -1:
            n = d.find(".")
        d2 = d[n + 1:]

        print len(d2), d2

        if len(d2) < 260:
            # wr.write("[]"+str(count)+"."+d2)
            wr.write("[]" + d2)
            count += 1
        else:
            dlong.append(d2)

    for dl in dlong:
        # wr.write("[]"+str(count)+"."+dl)
        wr.write("[]" + dl)
        count += 1
    wr.flush()
    wr.close()


# 处理程度副词
def fiter_xueqiu_zhi():
    """
    评论里面挑选出来副词 - 知网的挑出的程度副词
    """
    zhi = "/home/zhangxin/文档/市场情绪分析/情感词典/adeg.dict"
    xueqiu = "/home/zhangxin/文档/市场情绪分析/情感词典/评论副词_词频.txt"
    writer_result = open("/home/zhangxin/文档/市场情绪分析/情感词典/评论副词_词频_zhi.txt", "wb")

    zhi_data = []
    for d in open(zhi):
        temp = d.split(",")
        for t in temp:
            zhi_data.append(t.rstrip().lstrip())

    for d in open(xueqiu):
        t = d.split("\t")
        temp = t[0]
        if temp.__contains__("d"):
            word = temp[:temp.index("_")]
            if not zhi_data.__contains__(word):
                writer_result.write(word+"\t"+t[1])
        else:
            writer_result.write(word + "\t0\n")

    writer_result.flush()
    writer_result.close()

# 处理程度副词
def match_xueqiu_zhi_xueqiu():
    """
    从雪球评论中匹配出 含有 上面程度副词的评论,并输出
    :return:
    """
    xueqiu_zhi = "/home/zhangxin/文档/市场情绪分析/情感词典/评论副词_词频_zhi.txt"
    writer_result = open("/home/zhangxin/文档/市场情绪分析/情感词典/评论副词_词频_zhi_2.txt", "wb")

    zhi_data = []
    for d in open(xueqiu_zhi):
        if d.__contains__("\t"):
            temp = d.split("\t")
            zhi_data.append(temp[0])
        else:
            temp = d.strip("\n")
            zhi_data.append(temp)

    result = {}
    data = read_data.read_all(10)
    for d in data:
        for z in zhi_data:
            if d.get_content.__contains__(z):
                result[z] = result.get(z, "") + "\n\t\t" + d.get_content

    for r in result.keys():
        writer_result.write("[" + r + "]\t" + result[r] + "\n")

    writer_result.flush()
    writer_result.close()
    print len(result)

if __name__ == "__main__":
    match_xueqiu_zhi_xueqiu()
