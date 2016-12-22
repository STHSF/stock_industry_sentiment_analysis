# coding=utf-8
# -*- coding: <utf-8> -*-
# 主函数
import jieba
import re
import sqlite3
import json
import demjson
from data_prepare import corpus
from sentiment_intensity.STP import sentiment
from sentiment_intensity.STP import dicts
from sentiment_intensity.STP import read_data

conn = sqlite3.connect("/Users/li/workshop/DataSet/sentiment/xueqiuclear.db")
cu = conn.cursor()  # 创建游标
# query_str = "select created_at,clean_data from SH600004 where created_at='1440162062000'"
# query_str = "select created_at,clean_data from SH600004 where created_at='1451802826000'"
query_str = "select created_at,clean_data from SH600004"
cu.execute(query_str)
result = cu.fetchall()

comment_result = []

for i in result:
    print i[0]
    print i[1]
    time = i[0]
    res = demjson.decode(i[1].strip('\n'))
    print len(res)
    for j in xrange(len(res)):
        comment = res[j]['comment']
        print comment
        comment_result.append((time, comment))

# print comment_result[0][0]
# print comment_result[0][1]



#
# # comment = "这家酒店环境很不错,但是服务差"
#
# # 评论切句，构成情感单元
# sentiment_units = re.split(',|\.|，|。', comment)
#
# # 对情感单元分词
# sentiment_units_cut = []
# for j in sentiment_units:
#     res = corpus.units_cut(j)
#
#     # temp = res.decode("utf8")
#     res = corpus.filter_stop_word(res)
#     sentiment_units_cut.append(res)
#
#
# # 情感单元情感强度计算
#
# dicts.dict()
# for i in sentiment_units_cut:
#
#     print i
#     sentiment.compute(i)
#
# # 情感单元情感趋势计算


# if __name__ == '__main__':
