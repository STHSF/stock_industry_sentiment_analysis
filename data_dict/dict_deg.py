#!/usr/bin/env python
# encoding: utf-8
# -*- coding:utf-8 -*-

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: parser.py
# Time: 16-12-5 上午9:31
# -------------------------------------------
import jieba.posseg as pseg  # 需要另外加载一个词性标注模块
import data_processing.read_data as read


# 词性标注挑出句子的副词
def parser(sentence):
    result = []
    seg = pseg.cut(sentence)
    for s in seg:
        if s.flag.__contains__("d"):
            result.append((s.word, s.flag))

    return result


# 雪球数据 挑出句子副词
def xueqiu_parser():
    data = read.read_all(1000)
    word_d = {}
    writer = open("/home/zhangxin/文档/市场情绪分析/情感词典/评论副词_词频.txt", "wb")

    print "[总共]", len(data)
    for d in data:
        result = parser(d.get_content)
        print "\n%s" % d.get_content
        for r in result:
            print "   >> ", r[0], r[1]
            word_d[r[0] + "_" + str(r[1])] = word_d.get(r[0] + "_" + str(r[1]), 0) + 1

    word_d_list = sorted(word_d.iteritems(), key=lambda d: d[1], reverse=True)
    for l in word_d_list:
        writer.write(l[0] + "\t" + str(l[1]) + "\n")

    writer.flush()
    writer.close()


if __name__ == "__main__":
    # parser("我非常喜欢坤艳,我要为坤艳生很多猴子")
    # parser("多头今天死绝了么?")
    parser("妖气十足")
