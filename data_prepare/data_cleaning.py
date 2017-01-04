# coding=utf-8
import sqlite3
import demjson
from BeautifulSoup import BeautifulSoup


from BeautifulSoup import BeautifulSoup
import re

doc = ['二、北美和大陆医疗患者体验比较<br/><br/>我不懂医学，只是从患者体验的角度来说两者之间的区别比较。<br/><br/>1、大病复杂的病美国好一些，尤其是肿瘤什么的美国这边治疗好太多，这一点大家基本上有共识。这些年，我认识不少身体不好的老股民陆续有来美治复杂的病症或肿瘤，反应大体正面，当然费用也不低。<br/><br/>2、常见病、日常小毛病很多大陆看也许好一些，我们华人有些偶尔烦人的小毛病，比如喉咙卡刺啊什么的，大陆的普通医院的看病体验可以甩美国好多大医院几条街，细节我就不说了，谁经历过谁知道，美国人吃鱼没啥刺的问题，医生做的太少，经验太少。另外比如抽血， 美国的护士技术比较起上海北京的护士，水平只能说让人吐血，说起来都是泪。我有问过这边的医生，他们说大陆医院每天每个医生就诊量和美国这边不是一个数量级，护士那些抽血什么的上海一个护士一天做的比他们一个月做的都多，那些单纯依靠医生单个人手熟的小病小活，大陆比美国强太多太多。这个区别，导致不少移民到美国的同胞们多有抱怨。<br/><br/>3、转诊的等候时间北美过长，尤其是一些不紧急的慢性病症，这一点国内的媒体上也多有提及，不再赘述。<br/><br/><a href="http://xueqiu.com/S/SH601318" target="_blank">$中国平安(SH601318)$</a>&nbsp;&nbsp;<br><a href="http://xueqiu.com/S/SH600004" target="_blank">$白云机场(SH600004)$</a>&nbsp;&nbsp;<br><a href="http://xueqiu.com/S/SH600886" target="_blank">$国投电力(SH600886)$</a>&nbsp;&nbsp;<br><a href="http://xueqiu.com/S/SH600674" target="_blank">$川投能源(SH600674)$</a>&nbsp;&nbsp;<br><a href="http://xueqiu.com/S/SZ000568" target="_blank">$泸州老窖(SZ000568)$</a>']
# doc = '<a href="http://xueqiu.com/S/SZ000089" target="_blank">$深圳机场(SZ000089)$</a> 买入深圳机场、白云机场'


def remove_label(comment):
    """
    去除html中的标签等无用信息,替换干扰字符如"等
    :param comment:
    :return:
    """
    soup = BeautifulSoup(''.join(comment))
    html = soup.prettify()
    result = re.sub(r'(<a.*blank">)|(\n)|(<br />)|(&nbsp;)|(</a>)|\t|\s|(<img.*/>)', "", html)
    # res1 = re.sub(r'[\n\t\s]', "", res)
    # res2 = re.sub(r'(<br/>)|(&nbsp;)|(</a>)', "", res1)
    return result


# 读取sqlite数据
def read_sqlite(db_path, stock):
    conn = sqlite3.connect(db_path)
    cu = conn.cursor()
    # query_str = "select created_at,clean_data from %s WHERE created_at='1426662191000'" % stock
    query_str = "select text from %s" % stock
    cu.execute(query_str)
    result = cu.fetchall()
    comment_result = []
    try:
        for i in result:
            temp = remove_label(i)
            print temp
            print "\n"
    except:
        pass
    cu.close()
    conn.close()
    return comment_result


if __name__ == '__main__':
    db_path = "/Users/li/workshop/DataSet/sentiment/xueqiuclear.db"
    stock_list = 'SH6000' + '08'
    read_sqlite(db_path, stock_list)
