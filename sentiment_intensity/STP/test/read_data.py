#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：读取雪球评论数据, 进行测试
# Author: zx
# Software: PyCharm Community Edition
# File: read_data.py
# Time: 16-12-13 下午3:14
# -------------------------------------------
import jieba
import re
import sqlite3
import json
from sentiment_intensity.STP import sentiment, dicts


class jsonFile(object):
    """
    解析json文件，从json中把每个key对应的vlue解析出来，并且每层中key name相同的按照层数标示出来。
    """
    def __init__(self):
        self.contents = []
        self.i = 0

    def json_extract(self, json_file):
        # 判断传入的是否是json对象，不是json对象就返回异常
        try:
            if isinstance(json_file, dict):
                for key in json_file.keys():
                    key_value = json_file.get(key)
                    if isinstance(key_value, dict):
                        self.i += 1
                        self.json_extract(key_value)
                    elif isinstance(key_value, list):
                        for json_array in key_value:
                            self.i += 1
                            self.json_extract(json_array)
                    else:
                        self.contents.append((str(key)+'_'+str(self.i), str(key_value)))
            elif isinstance(json_file, list):
                for json_array in json_file:
                    self.json_extract(json_array)
        except:
            print "不是json格式，请检查正确的json格式。"
        finally:
            return self.contents


def comment_extract(temp):
    """
    解析从数据库中读取的内容,将数据中的所有评论解析出来,如果出现格式解析错误则返回NULL
    :param temp:
    :return:
    """
    if not isinstance(temp, list):
        print "数据错误，输入数据不是list格式"
    else:
        # 数据长度
        count = len(temp)
        print "总评论的条数：%s" % count
        comment_result = []
        # 逐条数据处理
        for row in xrange(count):
            rowid = temp[row][0]
            time = temp[row][1]
            comment = temp[row][2]
            # print 'rowid: %s,时间: %d' % (rowid, time)
            try:
                comments = json.loads(comment.decode('utf-8'))
                # 解析json数据，提取其中的评论内容。
                com = jsonFile()
                comment_list = com.json_extract(comments)
                # 识别评论内容,将评论中的所有评论内容（包括转发评论或者回复评论）都提取出来，并保持他们的结构。
                comment_id = []
                for i in comment_list:
                    comment_id.append(i[0])
                string = " ".join(comment_id)
                # print string
                content_index = re.findall(r'content_\d', string)
                # 提取出所有的评论内容，按照字典格式保存，便于后面的每条评论的逻辑计算。
                dicts.init()
                res_dic = {}
                # 计算小评论的条数
                content_index_len = len(content_index)
                # print "评论的个数：%s" % content_index_num
                # if content_index_num <= 1:
                #     res_dic[comment_list[content_index_num-1][0]] = sentiment.compute(comment_list[content_index_num-1][1])
                #     res_dic[comment_list[content_index_num-1][0]] = comment_list[content_index_num-1][1]
                # else:
                # 按照字典格式保存所有提取出来的评论。
                for index in xrange(content_index_len):
                    # 情感强度计算
                    # res_dic[comment_list[index][0]] = sentiment.compute(comment_list[index][1])
                    res_dic[comment_list[index][0]] = comment_list[index][1]
                    # print content_index[index], sentiment.compute(comment_list[index][1]), comment_list[index][1]
                    # print comment_list[index][0], comment_list[index][1]
                comment_result.append((rowid, res_dic))
            except:
                # 如果评论内容错误或者解析错误，则返回空值
                comment_result.append((rowid, {"NULL": "NULL"}))
                # print Exception
        return comment_result


def comment_compute(data):
    comment_result =[]
    if not isinstance(data, dict):
        print "数据格式错误，comment_compute"
    else:
        index = len(data)
        if index <= 1:
            comment_result.append(sentiment.compute(data.values()))
        else:
            for key in data.keys():
                print 0



        return 0



# 读取sqlite数据
def read_sqlite(db_path, query_str):
    """
    读取sqlite中的数据
    :param db_path: .db保存的路径
    :param query_str: 读取条件
    :return: list
    """
    conn = sqlite3.connect(db_path)
    cu = conn.cursor()
    try:
        cu.execute(query_str)
        result = cu.fetchall()
        return result
    except:
        print '数据库读取错误'
    finally:
        cu.close()
        conn.close()


# 读取本地雪球评论数据
def read_xueqiu():
    data_path = "/home/zhangxin/文档/市场情绪分析/基于依存句法分析/[筛选+标注]_以亿晶光电数据为例"

    data = []

    a = "\$.*?\$"
    for d in open(data_path):

        label = d[d.index("["):d.index("]") + 1]
        content = d[d.index("]") + 1:len(d)].strip("\n").strip(" ")
        content = re.sub(a, "", content)
        if len(content) < 200:
            print label, content
            data.append((label, content))

    return data


def test_data():
    sent10 = u'这是 一个 很 大 的 阴谋'
    sent11 = u'这 只 股票 涨 的 很 疯狂'
    sent5 = u'这 家 酒店 环境 但是 我 非常 不 他们 的 服务'
    sent1 = u'我 非常 不 喜欢 苹果'
    sent3 = u'我 非常 喜欢 苹果'
    sent7 = u'万科 涨停 了'
    sent8 = u'中铁 上涨 需要 新 的 炒作 题材'
    sent0 = u'猴子 喜欢 吃 香蕉'
    sent9 = u'我 非常 爱 苹果 , 但是 我 特别 讨厌 小米'
    sent2 = u"北海 已 成为 中国 对外开放 中 升起 的 一 颗 明星"

    sent11 = jieba.cut(u'这家酒店环境很不错, 但是服务差')  # -0.53(未做转折)   -0.74(转折)
    sent12 = jieba.cut(u'我非常看好这个')  # 1.95
    sent13 = jieba.cut(u'我看好这个')  # 1.3
    sent14 = jieba.cut(u'我不喜欢这个')  # -0.47
    sent15 = jieba.cut(u'我很不喜欢这个')  # -0.705
    sent16 = jieba.cut(u'这只股票会涨')  # 0 会涨分词没分开
    sent17 = jieba.cut(u'这只股票涨')  # 1.2
    sent18 = jieba.cut(u'这只股票看涨')  # 2.0
    sent19 = jieba.cut(u'这只股票看跌')  # -1.3
    sent20 = jieba.cut(u'这只股票肯定会跌')  # -1.24  有问题,可优化,,,'肯定'作为褒义词,未作程度词
    sent21 = jieba.cut(u'这只股票一定会跌')  # -1.63  '一定'作为贬义词, 未做程度副词
    sent22 = jieba.cut(u'这只股票一定涨')  # 0.97  '一定'作为贬义词
    sent23 = jieba.cut(u'理想很丰满，道路很曲折，我等还需耐心等待柳暗花明的一天')  # -0.0852
    sent24 = jieba.cut(u'我不很喜欢苹果')  # -0.705
    sent25 = jieba.cut(u'我失去你的喜欢')  # 句法分析报错
    sent26 = jieba.cut(u'我失去了他')  # 句法分析报错
    sent27 = jieba.cut(u'我喜欢你,但是不喜欢她')  # 句法分析报错
    sent28 = jieba.cut(u'我喜欢他,但是不喜欢她')  # -0.47
    sent29 = jieba.cut(u'我喜欢这家酒店的环境,但是不喜欢服务')  # -0.47
    sent = jieba.cut(u'拓日新能涨停，亿晶光电连续大涨')  # 1.70
    sent31 = jieba.cut(u'拓日新能涨停，亿晶光电连续大跌')  # 0.30

    str = " ".join(sent)
