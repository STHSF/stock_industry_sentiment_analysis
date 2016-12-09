# coding=utf-8
# 主函数

import re
from data_prepare import corpus

comment = "我喜欢女生，我爱中国,我讨厌日本。我不喜欢，复杂的东西."
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


for i in sentiment_units_cut:

    string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf-8"), "".decode("utf-8"), i)

    print string

print
# 情感单元情感趋势计算

# 情感单元情感强度计算



# if __name__ == '__main__':
