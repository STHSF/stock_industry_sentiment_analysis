# coding=utf-8
"""
数据清洗程序
解析程序，解析xueqiuclear.db中text里面的评论数据，将每条评论中所有的短评提取出来，没有区分评论是谁写的和评论发表的时间。
"""
import re
import sqlite3

from BeautifulSoup import BeautifulSoup

import corpus


def _comment_extract(text):
    m = re.split(r"//@.*?:", text)
    comments = []
    if m:
        for i in xrange(len(m)):
            r = re.split(r"回复@.*:", m[i])
            for j in xrange(len(r)):
                # print r[j], '\n'
                if 1 < len(r[j]) < 1000:   # 剔除空格和部分超长的句子
                    comments.append(r[j].strip())
    else:
        print 'not match'
    return comments


def _remove_label(comment):
    """
    去除html中的标签等无用信息,替换干扰字符如"等
    :param comment:
    :return:
    """
    soup = BeautifulSoup(''.join(comment))
    html = soup.prettify()
    # 剔除无用的标签、URL信息。
    temp = re.sub(r'(<a.*blank">)|(\n)|(<br />)|(&nbsp;)|(<a.*</a>)|\t|\s|(<img.*/>)|(<.*>)|(' ')', "", html)
    return temp


# 读取sqlite数据
def read_sqlite(db_path, stock_name):
    """
    读取sqlite中的数据，并且对每条数据进行评论提取
    :param db_path: 数据库路径
    :param stock_name: 表名
    :return:
    """
    conn = sqlite3.connect(db_path)
    cu = conn.cursor()
    # query_str = "select created_at,clean_data from %s WHERE created_at='1426662191000'" % stock_name
    query_str = "select text from %s" % stock_name
    cu.execute(query_str)
    query_res = cu.fetchall()
    # tmp = ['haohaoaho//@呼噜老K: 说的好//@ozrunner:回复@股市狂韭菜: 这些商业常识性的细节被很多人选择性忽视了。
    # 简单说，乐视群企业已经失去了商誉，很多人竟然还当他是个宝，害怕人低价强购，我乐个去啊']
    comment_result = []
    for index in xrange(len(query_res)):
        temp = _remove_label(query_res[index])
        comments = _comment_extract(temp)
        for j in comments:
            # print j
            comment_result.append(j)
    cu.close()
    conn.close()
    return comment_result


def add_column_sqlite(db_path, table_name, column_name):
    """
    数据库添加一个字段，并且每个value的值初始化为rowid
    :param db_path: 数据库路径
    :param table_name: 表名
    :param column_name: 新增字段的名字
    :return:
    """
    try:
        con = sqlite3.connect(db_path)
        cu = con.cursor()
        query_str = "select count(*) from %s" % table_name
        cu.execute(query_str)
        count = cu.fetchone()[0]

        cu.execute("ALTER TABLE %s ADD %s TEXT" % (table_name, column_name))
        for k in xrange(count):
            query_str2 = "update %s set %s = %d WHERE rowid=%d" % (table_name, column_name, k, k)
            cu.execute(query_str2)
        con.commit()
    except:
        print "字段增加错误"
    finally:
        con.close()
        cu.close()


if __name__ == '__main__':
    database_path = "/Users/li/workshop/DataSet/sentiment/xueqiuclear.db"
    for i in xrange(600):
        try:
            stock_list = 'SZ300%s' % i
            file_path = "/Users/li/workshop/DataSet/test/%s" % stock_list
            print stock_list
            print file_path
            tmp = read_sqlite(database_path, stock_list)
            corpus.write_content(tmp, file_path)
        except sqlite3.OperationalError:
            pass
