# coding=utf-8

from sklearn import linear_model
from sklearn import model_selection
import numpy as np
import pandas as pd
import globe
from gensim.models import Word2Vec
from sentiment_polarity.word2vec_model import word2vec_gensim_model
import chardet

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 训练集预处理，转换成词向量
file_path = '/Users/li/workshop/DataSet/sentiment_dic'
with open(file_path) as file_path:
    data = file_path.readlines()
    data_x = []
    data_y = []
    for i in range(len(data)):
        temp = data[i].strip().split(' ')
        data_x.append(temp[0])
        data_y.append(temp[1])

# data_x = ['中国', '美国', '日本']

data_list = []

for i in range(len(data_x)):
    data_list.append([data_x[i]])

n_dim = globe.n_dim
min_coun = globe.min_count

# word2vec model path
w2c_model_path = globe.w2c_model_path
word2vec_model = Word2Vec.load(w2c_model_path)

# word2vec_model = word2vec_gensim_model.built_word2vec_model(data_ll, n_dim, min_count)

# word2vec_model.build_vocab(data_x)
word2vec_model.train([['托单','托单', '托单','托单']])

# vec = np.zeros(size).reshape((1, n_dim))
# for word in data_x:
#     try:
#         data_list.append(word2vec_model[word].reshape(1, n_dim))
#     except KeyError:
#         word2vec_model.train_op(word)

print len(data_list)
print len(data_x)
# print len(data_y)

print word2vec_model['托单']
# print word2vec_model['中国']

# X_train, X_test, y_train, y_test = model_selection.train_test_split(data_list, data_y, test_size=0.1, random_state=0)
#
#

## 逻辑回归模型训练
# clf = linear_model.LinearRegression()
# clf.fit(X_train, y_train)
#
# res = clf.predict(X_test)
#
#
# for i in range(len(res)):
#     print res[i], y_test[i]
#
# ((y_test - clf.predict(X_test)) ** 2).sum()
#
# print('Test Accuracy: %.2f' % clf.score(y_test, label_test))
#