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
