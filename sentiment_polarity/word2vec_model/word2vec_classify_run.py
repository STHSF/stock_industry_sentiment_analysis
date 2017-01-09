# coding=utf-8
from gensim.models import Word2Vec
from sklearn.linear_model import SGDClassifier

import doc2vec_gensim_train
import globe
from data_processing import data_processing

# 读入数据
pos_file_path = globe.pos_file_path
neg_file_path = globe.neg_file_path
neu_file_path = globe.neu_file_path

pos_data = data_processing.read_source_data(pos_file_path)
neg_data = data_processing.read_source_data(neg_file_path)
neu_data = data_processing.read_source_data(neu_file_path)

res = data_processing.data_split(pos_data, neu_data, neg_data)
x_train = res[0]
x_test = res[1]
label_train = res[2]
label_test = res[3]
x_train = data_processing.text_clean(x_train)
x_test = data_processing.text_clean(x_test)

# 生成文本向量
n_dim = globe.n_dim
# word2vec model path
w2c_model_path = globe.w2c_model_path

word2vec_model = Word2Vec.load(w2c_model_path)
vecs = doc2vec_gensim_train.doc_vectors(x_train, x_test, n_dim, word2vec_model)
train_vecs = vecs[0]
test_vecs = vecs[1]


# 分类训练
lr = SGDClassifier(loss='hinge', penalty='l2')
lr.fit(train_vecs, label_train)

res = lr.predict(test_vecs)

for i in range(len(res)):
    print res[i], label_test[i]

print('Test Accuracy: %.2f' % lr.score(test_vecs, label_test))


# pre_prb = lr.predict_proba(test_vecs)[:, 1]

#
# fpr, tpr, _ = roc_curve(label_test, pre_prb)
# roc_auc = auc(fpr, tpr)
# plt.plot(fpr, tpr, label='area = %.2f' %roc_auc)
# plt.plot([0, 1], [0, 1], 'k--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.legend(loc='lower right')
#
# plt.show()

