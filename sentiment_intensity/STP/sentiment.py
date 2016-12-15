#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: sentiment.py
# Time: 16-12-12 下午1:46
# -------------------------------------------
<<<<<<< HEAD
=======
import parser_stanford as sfp
import nltk.tree as tree
import jieba
import globe
>>>>>>> ab11b5f3c85254ae01644e623a1dbf8519dc1c09
import sys
import dicts
import jieba
import parser_stanford as sfp

reload(sys)
sys.setdefaultencoding("utf-8")

<<<<<<< HEAD
=======
deg_dict = {}
senti_dict = {}
fou_dict = []
but_dict = []

# corpus_path_dic = {
#     'd_path': "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/程度副词_datatang.txt",
#     's_path': "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/[兰秋军]词典数据.txt",
#     'f_path': "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/fou.txt",
#     'b_path': "/home/zhangxin/文档/市场情绪分析/情感词典/stanford/but.txt"
# }

corpus_path_dic = globe.corpus_path_dic


# 读取词典
def read_dict():

    d_path = corpus_path_dic.get('d_path')  # 程度副词词典
    s_path = corpus_path_dic.get('s_path')  # 兰秋军数据词典
    f_path = corpus_path_dic.get('f_path')  # 否定词
    b_path = corpus_path_dic.get('b_path')  # 转折词

    for d in open(d_path):
        temp = d.decode("utf-8").split(" ")
        word_arr = temp[1].strip("\n").rstrip(" ").split("、")
        for w in word_arr:
            deg_dict[w] = temp[0]

    for d in open(s_path):
        d = d.decode("gbk")
        temp = d.split(" ")
        senti_dict[temp[0]] = float(temp[1])

    for d in open(f_path):
        d = d.decode("utf-8-sig")
        fou_dict.append(d.strip("\n"))

    for d in open(b_path):
        but_dict.append(d.strip("\n"))

>>>>>>> ab11b5f3c85254ae01644e623a1dbf8519dc1c09

# 计算情感值
def __com(tree):
    if tree.height() == 2:
        pos = tree.label()
        word = tree[0]
        print pos, word
        # tree.set_label(tree[0])
        # tree.pop()
        if pos == "AD" and dicts.deg_dict.has_key(word):
            return dicts.deg_dict[word], "*"
        elif pos == "AD" and dicts.fou_dict.__contains__(word):
            return 0, "-"
        elif dicts.senti_dict.has_key(word):
            return dicts.senti_dict[word], "+"
        elif dicts.but_dict.__contains__(word):
            return 0, "/"
        else:
            return 0, "+"

    else:
        t = tree

        temp = 0
        flag_out = "+"

        for i in range(len(t)):

            child = t[len(t) - i - 1]  # 先遍历右子树
            senti, flag_in = __com(child)
            senti = float(senti)

            print "| %5s |  %6.2f  |  %5s  |  %6.2f  |  %5s  |" % (child.label(), temp, flag_out, senti, flag_in)

            if flag_out == "/":  # 外层为转折词, 则不做改变
                temp = temp
                flag_out = "/"

            elif flag_in == "/":  # 内层为转折词, 则修改外层情感值 和 flag_out

                temp += senti
                flag_out = "/"

            elif flag_in == "+":

                temp += senti

            elif flag_in == "*":  # 程度副词

                if temp == 0:
                    temp = senti
                    flag_out = "*"
                else:
                    temp = float(senti) * float(temp)

            elif flag_in == "-":  # 否定词

                if temp == 0:
                    temp = senti
                    flag_out = "-"
                else:
                    temp = -temp

<<<<<<< HEAD
        return temp, flag_out


def compute(sentence):

    # 去停去空格，让句子过English词典
    sentence_filter = sentence.strip().replace("?", "").replace("!", "") \
        .replace(".", "").replace("。", "").replace("，", "")
    if dicts.eng_dict.has_key(sentence_filter):
        return dicts.eng_dict.get(sentence_filter, 0)

    # 分词
    seg = jieba.cut(sentence)
    string_seg = " ".join(seg)

    try:
        result = sfp.parser(string_seg)
        for r in result:
            print "|  %5s  | %6s |  %5s  | %6s |  %5s  |" % ("关系", "外层情感值", "外层操作", "内层情感值", "内层操作")
            result = __com(r)  # 计算情感值

            print result
            r.draw()
            return result

    except Exception:
        return "Kong"
=======
        return temp, flag2


if __name__ == "__main__":

    read_dict()

    print senti_dict.get(u'一定', 0)
    print senti_dict.get(u'肯定', 0)
    print senti_dict.get(u'跌', 0)
    print deg_dict.get(u'肯定', 0)
    print deg_dict.get(u'一定', 0)

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

    sent11 = jieba.cut(u'这家酒店环境很不错, 但是服务差')  # -0.53 未做转折
    sent12 = jieba.cut(u'我非常看好这个')  # 1.95
    sent13 = jieba.cut(u'我看好这个')  # 1.3
    sent14 = jieba.cut(u'我不喜欢这个，')  # -0.47
    sent15 = jieba.cut(u'我很不喜欢这个')  # -0.705
    sent16 = jieba.cut(u'这只股票会涨')  # 0 会涨分词没分开
    sent17 = jieba.cut(u'这只股票涨')  # 1.2
    sent18 = jieba.cut(u'这只股票看涨')  # 2.0
    sent19 = jieba.cut(u'这只股票看跌')  # -1.3
    sent20 = jieba.cut(u'这只股票肯定会跌')  # -1.24  有问题,可优化,,,'肯定'作为褒义词,未作程度词
    sent21 = jieba.cut(u'这只股票一定会跌')  # -1.63  '一定'作为贬义词, 未做程度副词
    sent22 = jieba.cut(u'这只股票一定涨')  # 0.97  '一定'作为贬义词
    sent = jieba.cut(u'理想很丰满，道路很曲折，我等还需耐心等待柳暗花明的一天')  # -0.0852

    str = " ".join(sent11)
    print str
    re = sfp.parser(str)  # 句法分析

    for r in re:
        r.pprint()  # 打印树

        result = com(r)  # 计算情感值
        print result

        # r.draw()

        # if flag == "+":
        #     temp += senti
        # elif child.label() == "AD" and flag == "-":  # 否定词
        #     temp = senti
        #     flag2 = "-"
        # elif child.label() == "AD" and flag == "*":  # 程度副词
        #     temp = senti
        #     flag2 = "*"
        # elif child.label() == "ADVP" and flag == "*":  # 程度副词
        #     if temp == 0:
        #         temp = senti
        #         flag2 = "*"
        #     else:
        #         temp = senti * temp
        # elif child.label() == "ADVP" and flag == "-":  # 否定词
        #     if temp == 0:
        #         temp = senti
        #         flag2 = "-"
        #     else:
        #         temp = -temp
>>>>>>> ab11b5f3c85254ae01644e623a1dbf8519dc1c09
