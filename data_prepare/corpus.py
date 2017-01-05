#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   中文预处理包括繁简转换，情感单元计算,中文分词，去除非utf-8字符等
   暂定使用jieba分词
"""

import jieba
import globe
import os
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')


class SentimentUnits(object):
    """
    情感（语义）单元计算
    将doc中的内容按照cut_list中的标点符号进行切割，分割成情感（语义）单元
    """

    def __init__(self, doc, cut_list):
        self.doc = doc
        self.cut_list = cut_list
        self.sentiment_units = []

    def find_token(self, char):
        """
        :param char: 目标字符
        :return: 目标字符是否存在于list中
        """
        if char in self.cut_list:
            return True
        else:
            return False

    def cut(self, lines):
        """
        切句，生成情感单元
        :param lines: 一条评论或者一篇文章
        :return: 情感单元列表
        """
        res = []
        line = []
        for row in lines:
            if self.find_token(row):
                line.append(row)
                res.append("".join(line))
                line = []
            else:
                line.append(row)
        return res

    def result(self):
        self.sentiment_units = []
        tmp = self.cut(list(self.doc.decode('utf-8')))
        for line in tmp:
            if line.strip() != "":
                self.sentiment_units.append(line.strip())
        # for sentence in self.sentiment_units:
        #     print sentence
        return self.sentiment_units


def units_cut(unit):
    """
    调用分词系统，对每个情感单元分词
    :param unit: 情感单元
    :return: 情感单元的分词结果，一个列表。
    """
    line = unit.strip().decode('utf-8', 'ignore')  # 去除每行首尾可能出现的空格，并转为Unicode进行处理
    word_list = list(jieba.cut(line))
    return word_list


def split_sentence(input_file, output_file):
    """
    从文件中读取文本内容，并对文本内容进行分词，然后将结果写入到另一个文件。
    :param input_file: 输入文件路径
    :param output_file: 输出文件路径
    :return: 分词结果并用逗号隔开写入文件。
    """
    fin = open(input_file, 'r')  # 以读的方式打开文件
    fout = open(output_file, 'w')  # 以写得方式打开文件

    for eachLine in fin:
        line = eachLine.strip().decode('utf-8', 'ignore')  # 去除每行首尾可能出现的空格，并转为Unicode进行处理
        # 用结巴分词，对每行内容进行分词,jieba.cut()返回的结构是一个可迭代的generator，可以用list(jieba.cut(...))转化为list
        word_list = list(jieba.cut(line))
        out_str = ''
        for word in word_list:
            out_str += word
            out_str += ','
        fout.write(out_str.strip().encode('utf-8') + '\n')  # 将分词好的结果写入到输出文件
    fin.close()
    fout.close()


def write_content(data, file_name):
    """
    将list数据写到指定的文件中
    :param data: list
    :param file_name: 文件目录+文件名
    :return:
    """
    file_out = open(file_name, 'a')
    for item in xrange(len(data)):
        try:
            string = str(item + 1) + '\t' + data[item]
            file_out.write(string.encode('utf-8') + "\n")
        except Exception:
            pass
    file_out.close()


# 文本处理
def sentence(file_parent_path):
    file_seg = {}
    for file_name in os.listdir(file_parent_path):
        file_path = os.path.join(file_parent_path, file_name)
        data = open(file_path)
        res = ""
        for d in data:
            temp = d.replace(" ", "").strip()
            res += filter_stop_word(list(jieba.cut(temp)))
        file_seg[file_name] = res
        data.close()
    return file_seg


count = 0


# 文本处理并写出
def sentence_out(file_parent_path, out):
    global count
    for file_name in os.listdir(file_parent_path):
        count += 1
        print '正在处理：', count
        file_path = os.path.join(file_parent_path, file_name)
        data = open(file_path)
        result = ""
        for d in data:
            temp = d.replace(" ", "").strip()
            result += filter_stop_word(list(jieba.cut(temp)))
        out.write(result + "\n")
        out.flush()
        data.close()


def filter_stop_word(cut_result):
    """
    过滤停用词
    :param cut_result:
    :return:
    """
    stopwords = {}.fromkeys([line.rstrip().encode('utf-8') for line in open(globe.stopword)])
    final = []
    for seg in cut_result:
        seg = seg.decode('utf-8')
        if seg not in stopwords:
            final.append(seg)
    final_str = "".join(final)  # 逗号隔开。
    return final_str


def do():
    input_txt = globe.input_txt
    output_txt = globe.output_txt
    # split_sentence(input_txt, output_txt)

    out_neg = open("/home/zhangxin/work/DeepSentiment/data/tagging/result_neg.txt", "wb")  # 写出文件
    out_neu = open("/home/zhangxin/work/DeepSentiment/data/tagging/result_neu.txt", "wb")  # 写出文件
    out_pos = open("/home/zhangxin/work/DeepSentiment/data/tagging/result_pos.txt", "wb")  # 写出文件

    sentence("/home/zhangxin/work/DeepSentiment/data/tagging/neg", out_neg)
    sentence("/home/zhangxin/work/DeepSentiment/data/tagging/neu", out_neu)
    sentence("/home/zhangxin/work/DeepSentiment/data/tagging/pos", out_pos)


# if __name__ == "__main__":
    # result = sentence('/home/zhangxin/work/workplace_python/DeepSentiment/data/predict_test/')
    # for r in result:
    #     print r

    # sentence = "我喜欢中国。我讨厌,日，本"
    #
    # res = re.split(",|。|，", sentence)
    # for i in res:
    #     print i
#

