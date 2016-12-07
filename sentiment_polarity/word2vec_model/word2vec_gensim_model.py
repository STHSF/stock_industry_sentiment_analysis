#!/usr/bin/env python
# coding:utf-8
# -*- coding: utf-8 -*-

"""
build word2vec model
"""
# import modules and logging
from gensim.models import Word2Vec
from multiprocessing import cpu_count
from data_prepare import data_processing
import logging
import globe
import sys

reload(sys)
sys.setdefaultencoding('utf8')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def built_word2vec_model(sentences, size, min_c):
    """
    word2vec model with the corpus
    :param sentences: list of sentences
    :param size: vector size
    :param min_c: min count
    :return: word2vec model
    """
    w2c_model = Word2Vec(size=size, min_count=min_c, workers=cpu_count())
    w2c_model.build_vocab(sentences)
    w2c_model.train(sentences)

    return w2c_model


def word2vec_test_zx():
    """
    输入txt文件，单篇doc占一行
    :return:
    """
    sentence_process = data_processing.MySentences(globe.data_process_result)
    n_dim = globe.n_dim
    min_count = 2
    model = built_word2vec_model(sentence_process, n_dim, min_count)
    model.save(globe.w2c_model_path)


def word2vec_test():

    # 读入数据
    pos_file_path = globe.pos_file_path
    neg_file_path = globe.neg_file_path
    neu_file_path = globe.neu_file_path
    neu_data = data_processing.read_source_data(neu_file_path)

    pos_data = data_processing.read_source_data(pos_file_path)
    neg_data = data_processing.read_source_data(neg_file_path)

    # tmp = data_processing.read_data(pos_file_path, neg_file_path)
    res = data_processing.data_split(pos_data, neu_data, neg_data)
    x_train = res[0]
    x_train = data_processing.text_clean(x_train)
    n_dim = 200
    min_count = 2
    model = built_word2vec_model(x_train, n_dim, min_count)
    model.save(globe.w2c_model_path)  # save model

    try:
        # var = model.similarity('油价', '原油')
        # print var
        # res = model.most_similar("油价")
        # for i in res:
        #     print i[0],
        #
        # print('\n')
        # dd = model.most_similar("原油")
        # for i in dd:
        #     print i[0],
        cc = model["原油"]
        print cc
    except KeyError:
        print("kkk")


if __name__ == "__main__":
    word2vec_test()

    # word2vec_test_zx()
