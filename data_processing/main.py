#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 16-11-24 上午9:55
# -------------------------------------------
import os
import json
import sys
import comment
import timestamp

reload(sys)
sys.setdefaultencoding('utf8')


def read_all():
    data_path = "/home/zhangxin/work/sentimentData"
    data_all_list = os.listdir(data_path)
    print len(data_all_list)
    data_all_map = {}
    for i in range(30000):
        temp = data_path + "/" + data_all_list[i]

        data = read_doc(temp)
        for d in data:
            # print d.get_id
            # print d.get_content
            # print d.get_stock
            # print "\n"
            if data_all_map.keys().__contains__(d.get_stock):
                temp_1 = data_all_map[d.get_stock]
                temp_1.append(d)
                data_all_map[d.get_stock] = temp_1
            else:
                temp_1 = [d]
                data_all_map[d.get_stock] = temp_1

    # 打印股票及对应的评论
    print "[总共股票] ", len(data_all_map)
    # for sk in data_all_map.keys():
    #     print "[", sk, "]"
    #     count = 1
    #     for c in data_all_map[sk]:
    #         print "  [", count, "]", c
    #         count += 1

    temp_sh600537 = data_all_map["SH600537"]
    print "[SH600537]"
    count = 1
    for c in temp_sh600537:
        print "  [", count, "]", "[", timestamp.stamp_2_time(c.get_time), "]", c.get_content
        count += 1


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

    return result


if __name__ == "__main__":
    read_all()
