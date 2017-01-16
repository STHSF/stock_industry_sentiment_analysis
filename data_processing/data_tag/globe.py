#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: globe.py
# Time: 16-11-18 下午2:52
# -------------------------------------------

# 类标
labels = ["1", "-1"]

# 当前类别
current_label = ""

# 全部新闻
docs = []
index = 0
batch_size = 1000
docs_all = []

# 当前新闻index
current_index = 0

# 写出到本地文件地址
output = "/home/zhangxin/work/workplace_python/stock_industry_sentiment_analysis/data_processing/data_tag/output/"

# sqlite 数据源

data_sqlite = "/home/zhangxin/文档/市场情绪分析/雪球数据/[剔除]data_xueqiu_sentiment_服务器_69.sqlite"