# coding=utf-8
# 主函数

from data_prepare import corpus

comment = "我喜欢女生，我爱中国,我讨厌日本,我不喜欢复杂的东西."
cut_list = [',', '.', '，']

# 评论切句，构成情感单元
re = corpus.SentimentUnits(comment, cut_list)
sentiment_units = []

for i in re.result():
    sentiment_units.append(i)

# 对情感单元分词
sentiment_units_cut = []
for j in sentiment_units:
    res = corpus.units_cut(j)
    res = corpus.filter_stop_word(res)
    sentiment_units_cut.append(res)


for i in sentiment_units_cut:
    print i

print
# 情感单元情感趋势计算

# 情感单元情感强度计算

# if __name__ == '__main__':
