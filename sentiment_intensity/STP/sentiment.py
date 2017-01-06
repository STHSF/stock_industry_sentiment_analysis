#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: sentiment.py
# Time: 16-12-12 下午1:46
# -------------------------------------------
import sys
import dicts
import jieba
import parser_stanford as sfp

reload(sys)
sys.setdefaultencoding("utf-8")

flag = False  # 限定词标记


# 计算情感值
def __com(tree):
    if tree.height() == 2:

        pos = tree.label()
        word = tree[0]

        if pos == "AD" and (word in dicts.deg_dict):
            return dicts.deg_dict[word], "*"
        elif pos == "AD" and dicts.fou_dict.__contains__(word):
            return 0.0, "-"
        elif word in dicts.senti_dict:
            return dicts.senti_dict[word], "+"
        elif dicts.but_dict.__contains__(word):
            return 0.0, "/"
        else:
            return 0.0, "+"

    else:
        temp = 0
        flag_out = "+"

        for i in range(len(tree)):

            child = tree[len(tree) - i - 1]  # 先遍历右子树
            senti, flag_in = __com(child)

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

        return temp, flag_out


# 计算情感值  考虑特殊限定词导致情感极性转移
def __com_limit(tree):
    global flag

    if tree.height() == 2:

        pos = tree.label()
        word = tree[0]

        tree.set_label(tree[0])
        tree.pop()

        if pos == "AD" and (word in dicts.deg_dict):
            return dicts.deg_dict[word], "*"
        elif pos == "AD" and dicts.fou_dict.__contains__(word):
            return 0.0, "-"
        elif word in dicts.senti_dict:
            if flag:
                flag = False
                return -(dicts.senti_dict[word]), "+"
            else:
                return dicts.senti_dict[word], "+"
        elif dicts.but_dict.__contains__(word):
            return 0.0, "/"
        elif dicts.lim_dict.__contains__(word):
            flag = True
            return 0.0, "+"
        else:
            return 0.0, "+"

    else:

        temp = 0
        flag_out = "+"

        for i in range(len(tree)):

            child = tree[len(tree) - i - 1]  # 先遍历右子树
            senti, flag_in = __com_limit(child)

            # print "| %5s |  %6.2f  |  %5s  |  %6.2f  |  %5s  |" % (child.label(), temp, flag_out, senti, flag_in)

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

        if tree.label() == "IP":  # Flag归负，保证限定词只作用于一个IP
            flag = False

        return temp, flag_out


def compute(sentence):
    # print sentence
    # 去停去空格，让句子过English词典
    sentence_filter = sentence.strip().replace("?", "").replace("!", "") \
        .replace(".", "").replace("。", "").replace("，", "")
    if sentence_filter in dicts.eng_dict:
        return dicts.eng_dict.get(sentence_filter, 0)

    # 分词
    seg = jieba.cut(sentence)
    string_seg = " ".join(seg)

    try:
        # 句法分析
        result = sfp.parser(string_seg)

        # 情感值计算
        global flag
        flag = False
        for r in result:
            result = __com_limit(r)
            return result[0]
    except Exception:
        return 0.0


# 单句测试
def compute_test(sentence):
    # 去停去空格，让句子过English词典
    sentence_filter = sentence.strip().replace("?", "").replace("!", "") \
        .replace(".", "").replace("。", "").replace("，", "")
    if sentence_filter in dicts.eng_dict:
        return dicts.eng_dict.get(sentence_filter, 0)

    # 分词
    seg = jieba.cut(sentence)
    string_seg = " ".join(seg)

    # 句法分析
    result = sfp.parser(string_seg)

    # 情感值计算
    global flag
    flag = False
    for r in result:
        print unicode(r)
        print "|  %5s  | %6s |  %5s  | %6s |  %5s  |" % ("关系", "外层情感值", "外层操作", "内层情感值", "内层操作")

        result = __com_limit(r)

        print result
        r.draw()
        return result[0]


# 已分词单句测试
def compute_seg(sentence):
    try:
        result = sfp.parser(sentence)
        for r in result:
            result = __com(r)  # 计算情感值
            return result[0]
    except Exception:
        return 0.0
