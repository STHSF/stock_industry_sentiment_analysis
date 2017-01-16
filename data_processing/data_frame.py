# coding=utf-8
"""
使用dataframe格式计算每条评论的情感强度，中间包含了去除无关评论、
"""
from pandas.io import sql
import sqlite3
import json
import re
from sentiment_intensity.STP import dicts
from sentiment_intensity.STP import sentiment
from sentiment_intensity.STP.test import read_data
from delete_no_use import delete_no_use


db_path = '/Volumes/Macintosh/dataset/stock_sentiment/discussclear.db'
table_name = 'SH600000'

conn = sqlite3.connect(db_path)
query_str = "select rowid, created_at, clean_data from %s" % table_name

# 生成dataframe格式数据
raw_df = sql.read_sql_query(query_str, conn)
conn.close()
text = raw_df.get('clean_data')
print "text length: %d" % len(text)
comment_result = []
for i in xrange(len(text)):
    comment = text[i]
    try:
        comments = json.loads(comment.decode('utf-8'))
        # 解析json数据，提取其中的评论内容。
        com = read_data.jsonFile()
        comment_list = com.json_extract(comments)
        # 识别评论内容,将评论中的所有评论内容（包括转发评论或者回复评论）都提取出来，并保持他们的结构。
        comment_id = []
        for i in comment_list:
            comment_id.append(i[0])
        string = " ".join(comment_id)
        # print "Json keys of every comment： %s" % string
        content_index = re.findall(r'content_\d', string)
        # 提取出所有的评论内容，按照字典格式保存，便于后面的每条评论的逻辑计算。
        dicts.init()
        res_dic = {}
        # 计算小评论的条数
        content_index_num = len(content_index)
        # print "评论的个数：%s" % content_index_num
        # 如果评论中包含短评的个数少于一个，直接返回值
        if content_index_num <= 1:
            # 评论过滤
            da = comment_list[content_index_num - 1][1]
            if delete_no_use.process(da):
                res = sentiment.compute(da)
                print "评论中只包含一条短评的结果：%s" % res
                comment_result.append(str(res))
            else:
                comment_result.append('NULL_COMMENT')
        else:
            # 按照字典格式保存所有提取出来的评论。
            num = 0
            for index in xrange(content_index_num):
                # 情感强度计算，将content_0的强度作为评论强度，极性取所有短评的逻辑乘。
                # 计算每条评论的
                data = comment_list[index][1]
                # 过滤评论结果，判断评论结果是不是满足要求
                if delete_no_use.process(data):
                    tmp = sentiment.compute(data)
                    res_dic[comment_list[index][0]] = tmp
                    if tmp < 0:
                        num += 1
                else:
                    res_dic[comment_list[index][0]] = 'NULL_COMMENT'
            # 如果第一个评论被判断为无效评论，该条评论结果为null
            if res_dic['content_0'] == 'NULL_COMMENT':
                comment_result.append('NULL')
                continue
            # 如果不是无效评论，则进行情感值计算
            elif num % 2 == 0:
                score = abs(res_dic['content_0'])
            else:
                score = - abs(res_dic['content_0'])
            print "评论中包含多条短评的结果: %s" % score
            comment_result.append(str(score))
    except:
        comment_result.append("NULL")
print len(comment_result)

# dataframe添加一列
raw_df['clean'] = comment_result
db_save_path = '/Volumes/Macintosh/dataset/stock_sentiment/discusscleartest.db'
co = sqlite3.connect(db_save_path)
raw_df.to_sql(table_name, co, if_exists='replace', index=False)
co.close()
print raw_df.head(10)

