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

# 添加stanford环境变量,此处需要手动修改，jar包地址为绝对地址。
os.environ['STANFORD_PARSER'] = '/Users/li/workshop/StanfordNLP/standford/jars/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/Users/li/workshop/StanfordNLP/standford/jars/stanford-parser-3.6.0-models.jar'

# 为JAVAHOME添加环境变量
# java_path = "C:/Program Files (x86)/Java/jdk1.8.0_11/bin/java.exe"
# os.environ['JAVAHOME'] = java_path

# 句法标注
# parser = stanford.StanfordParser(model_path=u"/Users/li/workshop/StanfordNLP/standford/jars/edu/chinesePCFG.ser.gz")
chi_parser = stanford.StanfordParser(u"/Users/li/workshop/StanfordNLP/standford/jars/stanford-parser.jar",
                                     u"/Users/li/workshop/StanfordNLP/standford/jars/stanford-parser-3.6.0-models.jar",
                                     u"/Users/li/workshop/StanfordNLP/standford/jars/edu/chinesePCFG.ser.gz")

# parser = stanford.StanfordParser(model_path=u"/home/zhangxin/work/stanford/jars/edu/englishPCFG.ser.gz")


res = list(chi_parser.parse(u'四川 已 成为 中国 西部 对外开放 中 升起 的 一 颗 明星'.split()))
for row in res[0].triples():
    print(row)