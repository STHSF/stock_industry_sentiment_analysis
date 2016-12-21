#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: test_pyltp.py
# Time: 16-12-20 下午8:14
# -------------------------------------------

from pyltp import Segmentor
from pyltp import Parser

# segmentor = Segmentor()  # 初始化实例
# segmentor.load('/home/zhangxin/work/LTP/ltp-models/3.3.1/ltp_data/cws.model')  # 加载模型
# words = segmentor.segment('元芳你怎么看')  # 分词
# print ','.join(words)
# segmentor.release()  # 释放模型


# words = ['我', '爱', '你']
# from pyltp import Postagger
#
# postagger = Postagger()  # 初始化实例
# postagger.load('/home/zhangxin/work/LTP/ltp-models/3.3.1/ltp_data/pos.model')  # 加载模型
# postags = postagger.postag(words)  # 词性标注
# # print '\t'.join(postags)
# postagger.release()  # 释放模型



import jieba.posseg as pseg

result = pseg.cut("元芳你怎么看")
words =[]
postags = []
for r in result:
    words.append(r.word)
    postags.append(r.flag)

parser = Parser() # 初始化实例
parser.load('/home/zhangxin/work/LTP/ltp-models/3.3.1/ltp_data/parser.model')  # 加载模型
arcs = parser.parse(words, postags)  # 句法分析
print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
parser.release()  # 释放模型
