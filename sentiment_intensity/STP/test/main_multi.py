#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 16-12-14 下午5:16
# -------------------------------------------
import time

import jieba

import read_data
import sentiment_intensity.STP.dicts as dicts
import sentiment_intensity.STP.sentiment as sentiment
import multiprocessing


def test_xueqiu_multi():

    data = read_data.read_xueqiu()[:50]

    print len(data)

    pool = multiprocessing.Pool(processes=4)
    for d in data:
        result = pool.apply_async(sentiment.compute, (d[1],))

    pool.close()
    pool.join()


def test_xueqiu():
    data = read_data.read_xueqiu()[:30]

    print len(data)

    for d in data:

        if not d[0].__contains__(u"观望"):
            result = sentiment.compute(d[1])

if __name__ == "__main__":
    begin = time.time()

    # 初始化五个词典
    dicts.init()

    test_xueqiu_multi()
    # test_xueqiu()

    print "%.3f" % ((time.time() - begin) / 60), "min"
