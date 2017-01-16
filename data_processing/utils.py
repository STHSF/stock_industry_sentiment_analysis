# coding=utf-8
import json
import sys
import re
import sqlite3
from sentiment_intensity.STP.test import read_data
from sentiment_intensity.STP import sentiment
import data_cleaning
reload(sys)
sys.setdefaultencoding("utf-8")

db_path = '/Volumes/Macintosh/dataset/stock_sentiment/discussclear.db'


def time_statistic(db_path):
    """
    统计所有股票中最早的评论创建的时间
    :param db_path:
    :return:
    """
    conn = sqlite3.connect(db_path)
    cu = conn.cursor()

    # 获取所有表名
    str_tb = "SELECT name FROM sqlite_master WHERE type='table' order by name"
    cu.execute(str_tb)
    result = cu.fetchall()
    table_name = [r[0] for r in result]
    print "股票数目：", len(table_name)
    result_ = []  # 所有股票评论最早发布的时间
    for stock in table_name:
        # print stock,
        str_query = "select created_at from %s ORDER BY created_at" % stock
        cu.execute(str_query)
        result = cu.fetchall()
        res = min(result)
        result_.append(res)

    cu.close()
    conn.close()
    print "评论最早发布时间：", min(result_)
    print "结果的长度：", len(result_)
