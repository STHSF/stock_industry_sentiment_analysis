# coding=utf-8

import globe
from gensim.models import Word2Vec
from sentiment_polarity.word2vec_model import word2vec_gensim_model

n_dim = globe.n_dim
min_count = globe.min_count

data_ll = [['aa'], ['bb'], ['cc'], ['dd'], ['ee']]

# word2vec model path
w2c_model_path = globe.w2c_model_path

word2vec_model = word2vec_gensim_model.built_word2vec_model(data_ll, n_dim, min_count)

word2vec_model.save(w2c_model_path)

model = Word2Vec.load(w2c_model_path)
# word2vec_model.build_vocab(data_x)
sentences = [['tt'], ['ww'], ['ee'], ['rr']]

model.train(sentences)

print model['aa']
