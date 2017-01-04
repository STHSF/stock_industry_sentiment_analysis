# coding=utf-8
# 情感强度计算

import STP.dicts as dicts
import STP.sentiment as sentiment


def calculate_sentence_list(sentence_list):
    """
    计算某时间段内评论的情感强度
    :param sentence_list: 评论集合
    :return: 情感强度
    """
    # 初始化五个词典
    dicts.init()

    sentiment_value_all = 0.0

    count = 0
    for s in sentence_list:
        sentiment_value = sentiment.compute(s)
        sentiment_value_all += sentiment_value
        if sentiment_value != 0.0:
            count += 1

    return sentiment_value_all/count


def calculate_sentence(sentence):
    """
    计算某条评论的情感强度和极性，极性阈值设置为0.3
    :param sentence: 评论
    :return: 极性和强度
    """
    # 初始化五个词典
    dicts.init()

    # 阈值
    point = 0.3

    sentiment_value = sentiment.compute(sentence)

    if sentiment_value >= point:
        return "pos", sentiment_value
    elif sentiment_value <= -point:
        return 'neg', sentiment_value
    else:
        return 'neu', sentiment_value
