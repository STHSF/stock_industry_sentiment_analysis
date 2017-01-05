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


def test_xueqiu():
    writer_result = open("/home/zhangxin/文档/市场情绪分析/基于依存句法分析/result_6.txt", "wb")

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

        if not d[0].__contains__(u"观望"):

            print "[正在执行]", count
            count += 1

            result = sentiment.compute(d[1])

            if d[0].__contains__(u"做多"):
                result_pos.append("%s\t[%6.2f]\t%s\t\n" % (d[0], result, d[1]))
            elif d[0].__contains__(u"看空"):
                result_neg.append("%s\t[%6.2f]\t%s\t\n" % (d[0], result, d[1]))

            if result > 0 and d[0].__contains__(u"做多"):
                count_p_r += 1
            elif result < 0 and d[0].__contains__(u"看空"):
                count_n_r += 1

            if result > 0:
                count_p += 1
            elif result < 0:
                count_n += 1

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
    sent = u'开抢了呵呵'
    sent = u'看来我要把你割了。一看就是没潜力'
    sent = u'好不容易碰到一个板，还被砸成这个样子，我也是醉了'
    sent = u'这留个缝让人上车是啥意思，怎么感觉是个陷阱'
    sent = u'小脸被打的噼噼的'
    sent = u'这只股票被打脸了'
    sent = u'，你是肿么了？预增那么多，还跌！'
    sent = u'又创新低了，跌得不成人形了！我最看好的之一，这是为什么呀?'
    sent = u'该发力了，大盘冲关就靠你了'
    sent = u'中石化赢利能力惊人'
    sent = u'糟糕的事情是油价涨了，股票跌了，两边损失'
    sent = u'这只股票跌得比谁都快'
    sent = u'昨天跑的太明智了'
    sent = u'暴跌是跌出机会来了，最后一粒子弹也打了亿晶光电'
    sent = u'下跌空间有限，建底仓'
    sent = u'买了就跌'
    sent = u'卖了就涨'
    sent = u'格力电器真是恨你不起来'
    sent = u'加仓呀，000875,600252,600537 。'
    sent = u'这只股票上涨空间有限'
    sent = u'心好累，这只股票就这样了'
    sent = u'我肚子饿了，我就不起来'
    sent = u'心好累，这只股票上涨空间有限'
    sent = u'龙头股份，涨不过大盘，靠'
    sent = u'格力电器真是爱不起来'
    sent = u'格力电器真是爱你不起来'

    result = sentiment.compute_test(sent)
    print result


def tese_lqj():
    pos_path = "/home/zhangxin/文档/市场情绪分析/文献/依存句法/兰秋军/TotalCorpus/pos/seg_positive.txt"
    neg_path = "/home/zhangxin/文档/市场情绪分析/文献/依存句法/兰秋军/TotalCorpus/neg/seg_negative.txt"

    count_pos = 0
    count_pos_right = 0

    count_neg = 0
    count_neg_right = 0

    for p in open(pos_path):
        p = p.decode("gbk").strip("\n")
        print "[正在执行 %d]" % count_pos, p
        r = sentiment.compute_seg(p)
        if r > 0:
            count_pos += 1
            count_pos_right += 1
        elif r < 0:
            count_neg += 1
        print r

    for n in open(neg_path):
        print "[正在执行neg %d]" % count_neg
        n = n.decode("gbk").strip("\n")
        r = sentiment.compute_seg(n)
        if r < 0:
            count_neg += 1
            count_neg_right += 1
        elif r > 0:
            count_pos += 1

    print "[POS] %d / %d = %.3f" % (count_pos_right, count_pos, float(count_pos_right) / count_pos)
    print "[NEG] %d / %d = %.3f" % (count_neg_right, count_neg, float(count_neg_right) / count_neg)


def test_xueqiu_stock(stock):
    url = "http"
    comment = read_data.read_sqlite(stock)
    for c in comment:
        print "\n---------------------"
        print c

        if not c.__contains__(url):
            r = sentiment.compute(c)
            if r > 0:
                print '[POS] %.3f' % r
            else:
                print '[NEG] %.3f' % r

        else:
            print '[该语句不是评论]'


def add_sentiment():
    word = {}
    for z in open("/home/zhangxin/文档/市场情绪分析/情感词典/服务器（雪球评论+知网）/zhi_neg_2(已经整理).txt"):
        z = z.decode("utf-8")
        z = z.split("\t")
        word[z[0]] = -0.5

    return word


if __name__ == "__main__":
    begin = time.time()

    # 初始化五个词典
    dicts.init()
    add_words = add_sentiment()
    temp = dict(dicts.senti_dict.items() + add_words.items())
    dicts.senti_dict = temp

    # test_xueqiu()

    test()

    # tese_lqj()

    # test_xueqiu_stock("SH600030")

    print "%.3f" % ((time.time() - begin) / 60), "min"

    # dict1 = {1: [1, 11, 111], 2: [2, 22, 222]}
    # dict2 = {3: [3, 33, 333], 4: [4, 44, 444]}
    #
    # dictMerged1 = dict(dict1.items() + dict2.items())
