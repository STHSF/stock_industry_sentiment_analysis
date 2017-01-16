# coding=utf-8
"""
将提取出来的所有评论整理，挑选出训练集
"""


def read_source_data(file_path):
    """
    读取文本文件.
    :param file_path:
    :return:
    """
    with open(file_path) as input_file:
        file_content = input_file.readlines()
        temp = []
        for row in file_content:
            temp.append(row)
    return file_content


if __name__ == "__main__":
    file_path = '/Volumes/Macintosh/dataset/stock_sentiment/test/SH600004'
    res = read_source_data(file_path)
    for i in res:
        print i
    print len(res)