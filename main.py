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
from sentiment_intensity.STP.test import read_data
from data_prepare import corpus

# db_path = "/Users/li/workshop/DataSet/sentiment/xueqiuclear.db"
# db_path = "/Users/li/Downloads/discuss.db"
db_path = '/Volumes/Macintosh/dataset/stock_sentiment/discussclear.db'
stock_list = 'SH6000' + '00'
# query_str = "select rowid, created_at, clean_data from %s WHERE created_at='1477008928000'" % stock
query_str = "select rowid, created_at, clean_data from %s" % stock_list

res = read_data.read_sqlite(db_path, query_str)
rr = read_data.comment_exact(res)

# corpus.write_content(res, "/Users/li/workshop/DataSet/test/test.txt")

#
# sentiment_units = "这家酒店环境很好,但是服务差"
#
# # 评论切句，构成情感单元
# sentiment_units = re.split('。', sentiment_units)
#
# # 对情感单元分词
# sentiment_units_cut = []
# for j in sentiment_units:
#     res = corpus.units_cut(j)
#     # temp = res.decode("utf8")
#     res = corpus.filter_stop_word(res)
#     sentiment_units_cut.append(res)
#
# # 情感单元情感强度计算
# dicts.init()
# for i in sentiment_units_cut:
#
#     print i
#     r = sentiment.compute(i)
#     print r


# if __name__ == '__main__':
