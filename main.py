# coding=utf-8
# 主函数
import jieba
import re
from data_prepare import corpus
from sentiment_intensity.STP import parser_stanford as sfp
from sentiment_intensity.STP import sentiment

comment = "这家酒店环境很不错， 但是服务差"
cut_list = [',', '.', '，', '。']

# 评论切句，构成情感单元
res = corpus.SentimentUnits(comment, cut_list)
sentiment_units = []

for i in res.result():
    sentiment_units.append(i)

# 对情感单元分词
sentiment_units_cut = []
for j in sentiment_units:
    res = corpus.units_cut(j)

    # temp = res.decode("utf8")
    res = corpus.filter_stop_word(res)
    sentiment_units_cut.append(res)


# 情感单元情感强度计算

sentiment.read_dict()

for i in sentiment_units_cut:

    print i
    # string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf-8"), " ".decode("utf-8"), i)

    re = sfp.parser(i)  # 句法分析

    for r in re:
        r.pprint()  # 打印树

        result = sentiment.com(r)  # 计算情感值
        print result

        # r.draw()

# 情感单元情感趋势计算


# if __name__ == '__main__':
