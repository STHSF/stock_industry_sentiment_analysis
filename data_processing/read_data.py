#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: read_data.py
# Time: 16-12-1 下午3:22
# -------------------------------------------
import os
import json
import sys
import comment
import timestamp

reload(sys)
sys.setdefaultencoding('utf8')


# 解析所有的json文件
def read_all_map():
    data_path = "/home/zhangxin/work/sentimentData_xueqiu"
    data_all_list = os.listdir(data_path)
    print len(data_all_list)
    data_all_map = {}  # [stock , [评论_1, 评论_2, ... 评论_n]]
    data_all = []  # 所有的评论
    for i in range(100000):
        temp = data_path + "/" + data_all_list[i]

        data = read_doc(temp)
        for d in data:

            # 处理:<股票 评论集合>
            if data_all_map.keys().__contains__(d.get_stock):
                temp_1 = data_all_map[d.get_stock]
                temp_1.append(d)
                data_all_map[d.get_stock] = temp_1
            else:
                temp_1 = [d]
                data_all_map[d.get_stock] = temp_1

            data_all.append(d)
    return data_all_map


# 解析指定数目的json文件
def read_all(n):
    data_path = "/home/zhangxin/work/sentimentData_xueqiu"
    data_all_list = os.listdir(data_path)
    print "[文件总共]", len(data_all_list)
    data_all = []  # 所有的评论
    count = 1
    for i in range(n):
        print "[读取_还剩下]", n - count
        count += 1
        temp = data_path + "/" + data_all_list[i]

        data = read_doc(temp)
        for d in data:
            data_all.append(d)

    return data_all


# 解析单个json文件
def read_doc(doc):
    result = []
    # 普通读取
    data = open(doc)
    for d in data:
        # 读取json文件
        s = json.loads(d)
        id = s[unicode("用户ID")]
        content = s[unicode("评论内容")]
        reply = s[unicode("被回复的人")]
        title = s[unicode("评论标题")]
        time = s[unicode("评论时间")]
        stock = s[unicode("股票代码")]

        com = comment.Comment(id, content, reply, title, time, stock)
        result.append(com)
    data.close()
    return result
