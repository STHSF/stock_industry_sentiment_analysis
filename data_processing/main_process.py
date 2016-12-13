#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 16-11-24 上午9:55
# -------------------------------------------
import read_data
import timestamp
import jieba
import dict
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 找出股票[H600537]相关的评论
def test_SH600537():
    data_all_map = read_data.read_all_map()
    print "[总共股票] ", len(data_all_map)
    temp_sh600537 = data_all_map["SH600537"]
    print "[SH600537]"
    count = 1
    for c in temp_sh600537:
        print "  [", count, "]", "[", timestamp.stamp_2_time(c.get_time), "]", c.get_content
        count += 1


# 构建基础词典:找出[评论中出现 + 知网情感词典]出现的情感词,以扩充领域情感词典
def find_dict():
    writer_pos = open("/home/zhangxin/文档/市场情绪分析/情感词典/zhi_pos.txt", "wb")
    writer_neg = open("/home/zhangxin/文档/市场情绪分析/情感词典/zhi_neg.txt", "wb")
    pos_word = {}
    neg_word = {}

    print "[正在读取数据]...."
    data_all = read_data.read_all(2)

    zhi_pos, zhi_neg = dict.get_dict()

    jieba.load_userdict("/home/zhangxin/文档/市场情绪分析/情感词典/知网/neg.txt")
    jieba.load_userdict("/home/zhangxin/文档/市场情绪分析/情感词典/知网/neg.txt")

    count = 1
    for d in data_all:
        seg = jieba.cut(d.get_content)
        print "[还剩下]", len(data_all) - count
        count += 1
        for s in seg:
            if zhi_pos.__contains__(s):
                pos_word[s] = pos_word.get(s, 0) + 1
            elif zhi_neg.__contains__(s):
                neg_word[s] = neg_word.get(s, 0) + 1

    pos_word = sorted(pos_word.iteritems(), key=lambda d: d[1], reverse=True)
    neg_word = sorted(neg_word.iteritems(), key=lambda d: d[1], reverse=True)

    for p in pos_word:
        writer_pos.write(p[0] + "\t" + str(p[1]) + "\n")

    for n in neg_word:
        writer_neg.write(n[0] + "\t" + str(n[1]) + "\n")

    writer_pos.flush()
    writer_neg.flush()
    writer_pos.close()
    writer_neg.close()
    print "[总共评论]", len(data_all)


# 构建程度词典: 研究评论中包含程度词的句子
def find_deg():
    writer_conment = open("/home/zhangxin/文档/市场情绪分析/情感词典/评论_deg.txt", "wb")
    conment_dict = {}

    print "[正在读取数据]...."
    data_all = read_data.read_all(1000)

    deg_dict = dict.get_dict_deg()
    #
    for d in deg_dict.keys():
        print len(d), "-", d, "-", deg_dict[d]

    jieba.load_userdict("/home/zhangxin/文档/市场情绪分析/情感词典/adeg.dict")

    count = 1
    for d in data_all:
        if len(d.get_content) < 250:
            seg = jieba.cut(d.get_content)
            print "[还剩下]", len(data_all) - count
            count += 1
            for s in seg:

                if deg_dict.keys().__contains__(s):
                    conment_dict[d.get_content] = deg_dict[unicode(s)]
                    # writer_conment.write("[" + deg_dict[unicode(s)] + "]" + "\t" + d.get_content + "\n")
                    break

    conment_list = sorted(conment_dict.iteritems(), key=lambda d: d[1], reverse=True)
    for c in conment_list:
        writer_conment.write("[" + c[1] + "]" + "\t" + c[0] + "\n")
    writer_conment.flush()
    writer_conment.close()


def run():
    dict = {'name': 1, 'Age': 2}
    dict['name'] = dict.get("name", 2) + 10
    print dict["name"]

    a = [1, 2, 3, 4, 5, 6]
    b = [2, 3]
    # if a.__contains__("")


    for d in dict.keys():
        print len(d), "-", d, "-", dict[d]


if __name__ == "__main__":
    find_deg()
