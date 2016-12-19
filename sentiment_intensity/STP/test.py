# coding=utf-8

import jieba
from sentiment_intensity.STP import sentiment
from sentiment_intensity.STP import dicts


dicts.dict()

sent = u'我对你特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别特别有信心，加油。'
# sent = u'今天不跌，但是明天会跌。'

re = sentiment.compute(sent)
