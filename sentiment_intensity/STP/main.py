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
    writer_result = open("/home/zhangxin/文档/市场情绪分析/基于依存句法分析/result_5.txt", "wb")

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

        result = sentiment.compute_seg(d[1])

        if d[0].__contains__(u"做多"):
            count_p += 1
        elif d[0].__contains__(u"观望"):
            count_a += 1
        elif d[0].__contains__(u"看空"):
            count_n += 1

        if d[0].__contains__(u"做多"):
            result_pos.append("%s\t[%6.2f]\t%s\t\n" % (d[0], result, d[1]))
        elif d[0].__contains__(u"看空"):
            result_neg.append("%s\t[%6.2f]\t%s\t\n" % (d[0], result, d[1]))
        elif d[0].__contains__(u"观望"):
            result_aaa.append("%s\t[%6.2f]\t%s\t\n" % (d[0], result, d[1]))

        if result > 0 and d[0].__contains__(u"做多"):
            count_p_r += 1
        elif result < 0 and d[0].__contains__(u"看空"):
            count_n_r += 1

        print "[Result]", result, count_p_r, count_n_r

    for p in result_pos:
        writer_result.write(p)
    for n in result_neg:
        writer_result.write(n)
    for a in result_aaa:
        writer_result.write(a)

    writer_result.flush()
    writer_result.close()

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
    sent = u'滴血的嘴唇露出嗜血的獠牙'
    sent = u'缩量明显，割肉盘加仓小晶，对它有信心'
    sent = u'缩量明显，割肉盘加仓小晶，对它有信心'
    sent = u'开抢了呵呵'

    re = sentiment.compute_seg(sent)
    print re


def tese_lqj():
    pos_path = "/home/zhangxin/文档/市场情绪分析/文献/依存句法/兰秋军/TotalCorpus/pos/seg_positive.txt"
    neg_path = "/home/zhangxin/文档/市场情绪分析/文献/依存句法/兰秋军/TotalCorpus/neg/seg_negative.txt"

    count_pos = 0
    count_pos_right = 0

    count_neg = 0
    count_neg_right = 0

    for p in open(pos_path):
        count_pos += 1
        print "[正在执行 %d]" % count_pos
        p = p.decode("gbk").strip("\n")
        r = sentiment.compute_seg(p)
        if r > 0:
            count_pos_right += 1

    print "\n>>>>>>>>>>>>>>>>>>>>>"
    print "[POS] %d / %d = %.3f" % (count_pos_right, count_pos, float(count_pos_right) / count_pos)
    print ">>>>>>>>>>>>>>>>>>>>>\n"

    for n in open(neg_path):
        count_neg += 1
        print "[正在执行neg %d]" % count_neg
        n = n.decode("gbk").strip("\n")
        r = sentiment.compute_seg(n)
        if r < 0:
            count_neg_right += 1

    print "[NEG] %d / %d = %.3f" % (count_neg_right, count_neg, float(count_neg_right) / count_neg)


if __name__ == "__main__":
    begin = time.time()

    # 初始化五个词典
    dicts.dict()

    # test_xueqiu()

    # test()

    # tese_lqj()

    print "%.3f" % ((time.time() - begin) / 60), "min"

    comment = read_data.read_sqlite()
    for c in comment:
        print "\n---------------------"
        print c

    # import json
    #
    # jf = '[{"comment": "什么是最近牛股特征？注意一下几个因素：入口、卡位、多业态、技术垄断。$乐视网(SZ300104)$ "}]'
    # jf1 = jf[jf.index("[")+1:jf.index("]")]
    # print jf1
    # j = json.loads(jf1)
    # print type(j)
    # print j['comment']

    # print len(u'你好')
    #
    # zhi_path = "/home/zhangxin/文档/市场情绪分析/情感词典/知网/pos.txt"
    # zhi = "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/zhi_pos.txt"
    # writer_zhi = open(zhi,"wb")
    #
    # for d in open(zhi_path):
    #     d = d.decode("utf-8").strip("\n")
    #     if len(d) > 2:
    #         print "%s  %d"%(d, len(d))
    #         writer_zhi.write(d+"\n")
    #
    # writer_zhi.flush()
    # writer_zhi.close()
