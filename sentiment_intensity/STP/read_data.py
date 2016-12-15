#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：读取雪球评论数据, 进行测试
# Author: zx
# Software: PyCharm Community Edition
# File: read_data.py
# Time: 16-12-13 下午3:14
# -------------------------------------------
import jieba
import re


# 读取本地雪球评论数据
def read_xueqiu():
    data_path = "/home/zhangxin/文档/市场情绪分析/基于依存句法分析/[筛选+标注]_以亿晶光电数据为例"

    data = []

    a = "\$.*?\$"
    for d in open(data_path):

        label = d[d.index("["):d.index("]") + 1]
        content = d[d.index("]") + 1:len(d)].strip("\n").strip(" ")
        content = re.sub(a, "", content)
        if len(content) < 200:
            print label, content
            data.append((label, content))

    return data


def test_data():
    sent10 = u'这是 一个 很 大 的 阴谋'
    sent11 = u'这 只 股票 涨 的 很 疯狂'
    sent5 = u'这 家 酒店 环境 但是 我 非常 不 他们 的 服务'
    sent1 = u'我 非常 不 喜欢 苹果'
    sent3 = u'我 非常 喜欢 苹果'
    sent7 = u'万科 涨停 了'
    sent8 = u'中铁 上涨 需要 新 的 炒作 题材'
    sent0 = u'猴子 喜欢 吃 香蕉'
    sent9 = u'我 非常 爱 苹果 , 但是 我 特别 讨厌 小米'
    sent2 = u"北海 已 成为 中国 对外开放 中 升起 的 一 颗 明星"

    sent11 = jieba.cut(u'这家酒店环境很不错, 但是服务差')  # -0.53(未做转折)   -0.74(转折)
    sent12 = jieba.cut(u'我非常看好这个')  # 1.95
    sent13 = jieba.cut(u'我看好这个')  # 1.3
    sent14 = jieba.cut(u'我不喜欢这个')  # -0.47
    sent15 = jieba.cut(u'我很不喜欢这个')  # -0.705
    sent16 = jieba.cut(u'这只股票会涨')  # 0 会涨分词没分开
    sent17 = jieba.cut(u'这只股票涨')  # 1.2
    sent18 = jieba.cut(u'这只股票看涨')  # 2.0
    sent19 = jieba.cut(u'这只股票看跌')  # -1.3
    sent20 = jieba.cut(u'这只股票肯定会跌')  # -1.24  有问题,可优化,,,'肯定'作为褒义词,未作程度词
    sent21 = jieba.cut(u'这只股票一定会跌')  # -1.63  '一定'作为贬义词, 未做程度副词
    sent22 = jieba.cut(u'这只股票一定涨')  # 0.97  '一定'作为贬义词
    sent23 = jieba.cut(u'理想很丰满，道路很曲折，我等还需耐心等待柳暗花明的一天')  # -0.0852
    sent24 = jieba.cut(u'我不很喜欢苹果')  # -0.705
    sent25 = jieba.cut(u'我失去你的喜欢')  # 句法分析报错
    sent26 = jieba.cut(u'我失去了他')  # 句法分析报错
    sent27 = jieba.cut(u'我喜欢你,但是不喜欢她')  # 句法分析报错
    sent28 = jieba.cut(u'我喜欢他,但是不喜欢她')  # -0.47
    sent29 = jieba.cut(u'我喜欢这家酒店的环境,但是不喜欢服务')  # -0.47
    sent = jieba.cut(u'拓日新能涨停，亿晶光电连续大涨')  # 1.70
    sent31 = jieba.cut(u'拓日新能涨停，亿晶光电连续大跌')  # 0.30

    str = " ".join(sent)
