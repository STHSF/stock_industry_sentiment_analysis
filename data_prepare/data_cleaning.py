# coding=utf-8
"""
解析程序，解析xueqiuclear.db中text里面的评论数据，将每条评论中所有的短评提取出来，没有区分评论是谁写的或者评论发表的时间。
"""
import sqlite3
import demjson
from BeautifulSoup import BeautifulSoup
import re
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
def read_sqlite(fdb_path, stock):
    conn = sqlite3.connect(db_path)
    cu = conn.cursor()
    # query_str = "select created_at,clean_data from %s WHERE created_at='1426662191000'" % stock
    query_str = "select text from %s" % stock
    cu.execute(query_str)
    tmp = cu.fetchall()
    # tmp = ['haohaoaho//@呼噜老K: 说的好//@ozrunner:回复@股市狂韭菜: 这些商业常识性的细节被很多人选择性忽视了。
    # 简单说，乐视群企业已经失去了商誉，很多人竟然还当他是个宝，害怕人低价强购，我乐个去啊']
    comment_result = []
    for i in xrange(len(tmp)):
        temp = _remove_label(tmp[i])
        comments = _comment_extract(temp)
        for j in comments:
            # print j
            comment_result.append(j)
    cu.close()
    conn.close()
    return comment_result


def save2sqlite():
    return 0


if __name__ == '__main__':
    db_path = "/Users/li/workshop/DataSet/sentiment/xueqiuclear.db"
    for i in xrange(600):
        try:
            stock_list = 'SZ300%s' % i
            file_path = "/Users/li/workshop/DataSet/test/%s" % stock_list
            print stock_list
            print file_path
            tmp = read_sqlite(db_path, stock_list)
            corpus.write_content(tmp, file_path)
        except sqlite3.OperationalError:
            pass
