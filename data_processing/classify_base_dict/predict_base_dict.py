#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能： 基于词典的情感分析
# Author: zx
# Software: PyCharm Community Edition
# File: predict_base_dict.py
# Time: 17-1-4 上午9:49
# -------------------------------------------
import jieba


# 否定词翻转
def __count_sentiment(index, seg, fou_dict):

    # 寻找情感词前面的否定词，若有则返回-1
    if index - 1 > 0:
        if seg[index-1] in fou_dict:
            return -1
        elif index - 2 > 0:
            if seg[index-2] in fou_dict:
                return -1

    # 寻找情感词后面的否定词，若有则返回-1
    if index + 1 < len(seg):
        if seg[index + 1] in fou_dict:
            return -1
        elif index + 2 < len(seg):
            if seg[index + 2] in fou_dict:
                return -1

    return 1


# 情感分析
def predict(sentence, pos_dict, neg_dict, fou_dict):

    positive = 0.0
    negative = 0.0

    seg = jieba.cut(sentence)
    seg = list(seg)
    for s in seg:
        index = seg.index(s)

        if s in pos_dict:
            if __count_sentiment(index, seg, fou_dict) >0:
                positive += 1
            else:
                negative += 1
        elif s in neg_dict:
            if __count_sentiment(index, seg, fou_dict) >0:
                negative += 1
            else:
                positive += 1

    if positive > negative:
        return 1
    elif positive < negative:
        return -1
    else:
        return 0
