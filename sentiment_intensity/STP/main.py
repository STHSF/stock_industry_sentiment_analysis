#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 16-12-14 下午5:16
# -------------------------------------------
import sentiment
import read_data
import jieba
import time
import dicts


def test_xueqiu():
    # writer_result = open("/home/zhangxin/文档/市场情绪分析/基于依存句法分析/result_4.txt", "wb")

    data = read_data.read_xueqiu()

    # 统计准确性
    count_p = 0
    count_n = 0
    count_a = 0

    count_p_r = 0
    count_n_r = 0
    count_a_r = 0

    result_pos = []
    result_neg = []
    result_aaa = []

    print len(data)
    count = 1
    for d in data:

        print "[正在执行]", count
        count += 1

        result = sentiment.compute(d[1])

        if d[0].__contains__(u"做多"):
            count_p += 1
        elif d[0].__contains__(u"观望"):
            count_a += 1
        elif d[0].__contains__(u"看空"):
            count_n += 1

        if d[0].__contains__(u"做多"):
            result_pos.append("%s\t[%6.2f]\t%s\t\n" % (d[0], result[0], d[1]))
        elif d[0].__contains__(u"看空"):
            result_neg.append("%s\t[%6.2f]\t%s\t\n" % (d[0], result[0], d[1]))
        elif d[0].__contains__(u"观望"):
            result_aaa.append("%s\t[%6.2f]\t%s\t\n" % (d[0], result[0], d[1]))

        if result[0] > 0 and d[0].__contains__(u"做多"):
            count_p_r += 1
        elif result[0] < 0 and d[0].__contains__(u"看空"):
            count_n_r += 1

        print "[Result]", result, count_p_r, count_n_r

    # for p in result_pos:
    #     writer_result.write(p)
    # for n in result_neg:
    #     writer_result.write(n)
    # for a in result_aaa:
    #     writer_result.write(a)
    #
    # writer_result.flush()
    # writer_result.close()

    print "[看多] ", count_p, count_p_r, float(count_p_r) / float(count_p)

    print "[看空] ", count_n, count_n_r, float(count_n_r) / float(count_n)


def test():
    sent = jieba.cut(u'送股未到账，小散已先死')
    sent = jieba.cut(u'终于开始挖坑了，好现象，等')
    sent = jieba.cut(u'坐等周二继续跌，完了再补仓。啦啦啦，25.2的t做的好')
    sent = jieba.cut(u'这个位置不起来就危险了，最后一道防线是前面构筑的平台')
    sent = jieba.cut(u'大盘下挫的我好心疼')
    sent = jieba.cut(u'这个位置不起来就危险了')
    sent = jieba.cut(u'你是谁')
    sent = jieba.cut(u'这只股票非常好')
    sent = jieba.cut(u'我配不上你的喜欢')
    sent = jieba.cut(u'下跌，加仓')
    sent = jieba.cut(u'非公开发行审核通过')
    sent = jieba.cut(u'只有做正确的事情才能赚钱，不管你是不是只是暂时错了，割掉。亿晶光电，软控股份')
    sent = jieba.cut(u'这周不错，加油！')
    sent = jieba.cut(u'庄家选择了最激烈的方法…不过趋势在…无所谓的事…')
    sent = jieba.cut(u'你很美丽，不过我喜欢她')
    sent = jieba.cut(u'龙头股份，涨不过大盘，靠')

    sent = u'good'
    sent = u'fuck'
    sent = u'今天能收红吗，艹'
    sent = u'开抢了呵呵'
    sent = u'滴血的嘴唇露出嗜血的獠牙'
    sent = u'缩量明显，割肉盘加仓小晶，对它有信心'
    sent = u'缩量明显，割肉盘加仓小晶，对它有信心'

    re = sentiment.compute(sent)
    print re


if __name__ == "__main__":
    begin = time.time()

    # 初始化五个词典
    dicts.dict()

    # test_xueqiu()

    # test()

    print "%.3f" % ((time.time() - begin) / 60), "min"

    writer_pos = open(u"/home/zhangxin/文档/市场情绪分析/情感词典/stanford/senti_pos.txt", "wb")
    writer_neg = open(u"/home/zhangxin/文档/市场情绪分析/情感词典/stanford/senti_neg.txt", "wb")

    pos = {}
    neg = {}
    for d in dicts.senti_dict.keys():
        if dicts.senti_dict[d] > 0:
            pos[d] = dicts.senti_dict[d]
        else:
            neg[d] = dicts.senti_dict[d]

    sort_pos = sorted(pos.iteritems(), key=lambda d: d[1], reverse=True)
    sort_neg = sorted(neg.iteritems(), key=lambda d:d[1], reverse=True)

    for p in sort_pos:
        writer_pos.write(p[0]+"\t"+str(p[1])+"\n")

    for n in sort_neg:
        writer_neg.write(n[0]+"\t"+str(n[1])+"\n")

    writer_pos.flush()
    writer_neg.flush()
    writer_pos.close()
    writer_neg.close()