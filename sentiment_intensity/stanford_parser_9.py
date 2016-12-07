#!/usr/bin/env python
# encoding: utf-8
# -*- coding:utf-8 -*-

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: stanford_parser.py
# Time: 16-12-5 上午11:30
# -------------------------------------------
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import chardet

# 3
import os
from nltk.parse import stanford

#添加stanford环境变量,此处需要手动修改，jar包地址为绝对地址。
os.environ['STANFORD_PARSER'] = '/home/zhangxin/work/stanford/jars/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/home/zhangxin/work/stanford/jars/stanford-parser-3.6.0-models.jar'


#为JAVAHOME添加环境变量
# java_path = "C:/Program Files (x86)/Java/jdk1.8.0_11/bin/java.exe"
# os.environ['JAVAHOME'] = java_path

#句法标注
parser = stanford.StanfordParser(model_path=u"/home/zhangxin/work/stanford/jars/edu/chinesePCFG.ser.gz")

parser = stanford.StanfordParser(model_path=u"/home/zhangxin/work/stanford/jars/edu/englishPCFG.ser.gz")

# sentences = parser.parse_sents("我爱中国,我爱坤艳.".split(), "What is your name?".split())
# sentences = parser.parse_sents("我爱中国,我爱坤艳.".decode("utf-8").split())
# s = unicode("我爱中国")
s = "hello, everyone , i love china"
# print chardet.detect(s)
sentences = parser.parse_sents(s.split())
for s in sentences:
    print s
    for ss in s:
        print ss
        for sss in ss:
            print sss

# GUI
# for sentence in sentences:
#     sentence.draw()

# 2
# from nltk.parse import stanford
# parser=stanford.StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
# list(parser.raw_parse("the quick brown fox jumps over the lazy dog"))


# 1
# from nltk.parse import stanford
# import os
#
#
# def parser2():
#     os.environ["STANFORD_PARSER"] = "stanford-parser.jar"
#     os.environ["STANFORD_MODELS"] = "/home/zhangxin/work/stanford/stanford-chinese-corenlp-2016-01-19-models.jar"
#
#     s = "我爱坤艳,我要给坤艳生一堆儿子"
#     parser = stanford.StanfordParser(model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
#     r = parser.raw_parse_sents(
#         ("the quick brown fox jumps over the lazy dog", "the quick grey wolf jumps over the lazy fox"))
#
#     print r
#
# if __name__ == "__main__":
#     parser2()



# 4
# from nltk.internals import find_jars_within_path
# from nltk.parse.stanford import StanfordDependencyParser
# dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
# stanford_dir = st._stanford_jar.rpartition('/')[0]
# # or in windows comment the line above and uncomment the one below:
# #stanford_dir = st._stanford_jar.rpartition("\\")[0]
# stanford_jars = find_jars_within_path(stanford_dir)
# st.stanford_jar = ':'.join(stanford_jars)
# [parse.tree() for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")]