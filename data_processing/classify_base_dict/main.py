#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：基于词典的情感计算
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 17-1-4 上午10:12
# -------------------------------------------
import predict_base_dict as predicts
import dicts
import sqlite3
import os
import re


def run():
    data_path = "/home/zhangxin/文档/市场情绪分析/雪球数据/test"
    file_list = os.listdir(data_path)
    a = "\$.*?\$"

    conn = sqlite3.connect(
        "/home/zhangxin/文档/市场情绪分析/雪球数据/data_xueqiu_sentiment.sqlite")
    cu = conn.cursor()

    result = {}

    for f in file_list:

        conn.execute("create table IF NOT EXISTS %s(id,content,senti)" % f)  # 建表
        count = 0
        for d in open(data_path + "/" + f):
            try:
                count += 1
                temp = d.strip("\n").split("\t")
                d = re.sub(a, "瓜达尔", temp[1])
                sentiment = predicts.predict(d, dicts.pos_dict, dicts.neg_dict, dicts.fou_dict)

                senti = 0
                if sentiment > 0:
                    senti = 1
                elif sentiment < 0:
                    senti = -1

                str = "insert into %s values('%s','%s','%s')" % (f, count, temp[1], senti)
                conn.execute(str)  # 插入数据

                conn.commit()
            except Exception:
                print "[异常]>>>>>>>>>>>>>"

        print f, " : ", count
        result[f] = count

    conn.close()
    cu.close()
    for r in result.keys():
        print r, ": ", result[r]


if __name__ == '__main__':
    dicts.init()
    run()
