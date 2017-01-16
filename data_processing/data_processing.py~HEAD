#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""生成词向量空间"""

from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
import numpy as np
import logging
import os

import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# sentencestest = [['中国', '人'], ['美国', '人']]
# # train word2vec on the two sentences
# model = gensim.models.Word2Vec(sentences, min_count=1)
#
# print model["中国"]


# class MySentences1(object):
#
#     def __init__(self, dir_name):
#         self.dir_name = dir_name
#         self.do()
#
#     def do(self):
#         res = []
#         for file_name in os.listdir(self.dir_name):
#             for line in open(os.path.join(self.dir_name, file_name)).readlines():
#                 res.append(line.strip())
#         return res

# #  a memory-friendly iterator
# sentences = MySentences('/Users/li/Kunyan/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data')
# sentences = MySentences('/Users/li/Kunyan/DataSet/trainingSets')  # a memory-friendly iterator

# 读取文件夹中的所有数据
class MySentences(object):
    def __init__(self, dir_name):
        self.dir_name = dir_name

    def __iter__(self):
        for line in open(self.dir_name):
            yield line.split(",")


# 读取文件夹中的所有数据_兰秋军评论数据
class MySentences_lqj(object):
    def __init__(self, dir_name):
        self.dir_name_list = os.listdir(dir_name)
        self.dir_name = dir_name

    def __iter__(self):
        for f in self.dir_name_list:
            for d in open(self.dir_name + "/" + f):
                d = d.decode("gbk").replace("，", "").strip("\n").split(" ")
                yield d


import data_json
import jieba


# 读取雪球评论数据_ 廖成名数据集
class MySentences_lcm(object):
    def __init__(self):
        temp = data_json.read_all(80000)
        self.data = [c.get_content for c in temp]

    def __iter__(self):
        # for d in self.data:
        #     dseg = list(jieba.cut(d))
        #     yield dseg

        pattern_stock = '\$.*\$'
        pattern_num = "\d+"

        char = {u"，", u"：", u"？", u",", u".", u"!", u"！", u"、", u',',
                "%", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        for content in self.data:
            content = content.replace(" ", "").replace("-", "")
            content = re.sub(pattern_stock, ",", content)
            content = re.sub(pattern_num, ",", content)
            b = list(jieba.cut(content))

            for bb in b:
                if bb in char:
                    b.remove(bb)

            yield b


def read_source_data(file_path):
    """
    读取文本文件，文本已经进行分词且词之间用逗号隔开。
    :param file_path:
    :return:
    """
    with open(file_path) as input_file:
        file_content = input_file.readlines()
        temp = []
        for row in file_content:
            t = row.split(",")
            for i in t:
                temp.append(i)
    return file_content


# 按照标签读取数据
def read_data(pos_file_path, neg_file_path):
    with open(pos_file_path) as input_file:
        pos_file = input_file.readlines()
        tmp = []
        for i in pos_file:
            tmp.append(i.split(","))

    with open(neg_file_path) as input_file:
        neg_file = input_file.readlines()
        tmp = []
        for i in pos_file:
            tmp.append(i.split(","))

    res = (pos_file, neg_file)
    return res


def data_split(pos_file, neu_file, neg_file):
    """
    数据预处理,设置训练集和测试集的标签, 训练集测试集准备
    :param neu_file:
    :param pos_file:
    :param neg_file:
    :return:
    """
    # 设置标签
    label = np.concatenate((np.ones(len(pos_file)), np.zeros(len(neu_file)), 1 + np.ones(len(neg_file))))
    # 从训练集中抽取一部分数据作为测试集，即将原始数据分成训练集和测试集两部分。
    train_data, test_data, train_labels, test_labels = train_test_split(np.concatenate((pos_file, neu_file, neg_file)),
                                                                        label,
                                                                        test_size=0.1)
    res = (train_data, test_data, train_labels, test_labels)
    return res


def text_clean(corpus):
    """
    字符串清理，去除换行符。
    """
    corpus = [z.lower().strip().replace('\n', ' ').split(',') for z in corpus]
    return corpus


# 测试
def do():
    sen = MySentences("/home/zhangxin/work/DeepSentiment/data/tagging/result.txt")
    count = 1
    for s in sen:
        print count, " ".join(s)
        count += 1


def process_lcm():
    a = data_json.read_all(5)
    pattern_stock = '\$.*\$'
    pattern_num = "\d+"

    char = {u"，", u"：", u"？", u",", u".", u"!", u"！", u"、", u',',
            "%", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    for aa in a:
        content = aa.get_content
        content = content.replace(" ", "")
        content = re.sub(pattern_stock, ",", content)
        content = re.sub(pattern_num, ",", content)
        b = list(jieba.cut(content))

        for bb in b:
            if bb in char:
                b.remove(bb)

                # print "\n", content

        if len(b) > 0:
            print b
            print "[SEG]", ",".join(b)

    return b


if __name__ == "__main__":
    # do()
    # re = read_source_data('/Users/li/workshop/DataSet/sentiment/train/test.txt')
    # print type(re[0])
    # for i in re[0]:
    #     print i
    process_lcm()
