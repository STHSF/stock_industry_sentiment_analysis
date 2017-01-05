#!/usr/bin/env python
# coding:utf-8
# -*- coding: utf-8 -*-

# 全局变量模块

# corpus
# input_txt = '/home/zhangxin/work/workplace_python/DeepNaturalLanguageProcessing/DeepNLP/data/input/myInput.txt'
# output_txt = '/home/zhangxin/work/workplace_python/DeepNaturalLanguageProcessing/DeepNLP/data/input/myOutput.txt'
stopword = '/home/zhangxin/work/workplace_python/stock_industry_sentiment_analysis/data_warehouse/stopword.txt'
# stopword = '/Users/li/workshop/MyRepository/stock_industry_sentiment_analysis/data_warehouse/stopword.txt'


# data_patent = ''
# data_process_result = '/home/zhangxin/work/workplace_python/DeepSentiment/data/tagging/result.txt'
#
# # train_op
#
# train_data = ('neg', '/home/zhangxin/work/DeepSentiment/data/train_op/result_neg.txt')
# train_neu = ('neu', '/home/zhangxin/work/DeepSentiment/data/train_op/result_neu.txt')
# train_pos = ('pos', '/home/zhangxin/work/DeepSentiment/data/train_op/result_pos.txt')

# train_data = [(1, '/home/zhangxin/work/DeepSentiment/data/train_op/result_neg.txt'),
#               (2, '/home/zhangxin/work/DeepSentiment/data/train_op/result_neu.txt'),
#               (3, '/home/zhangxin/work/DeepSentiment/data/train_op/result_pos.txt')]

# train_data = [(0, '/home/zhangxin/work/DeepSentiment/data/train_op/result_neg.txt'),
#               (1, '/home/zhangxin/work/DeepSentiment/data/train_op/result_pos.txt')]
#
# file_parent = '/home/zhangxin/work/workplace_python/DeepNaturalLanguageProcessing/DeepNLP/data'
# file_pos = '/home/zhangxin/work/workplace_python/DeepNaturalLanguageProcessing/DeepNLP/data/test3.txt'
# file_neg = '/home/zhangxin/work/workplace_python/DeepNaturalLanguageProcessing/DeepNLP/data/test2.txt'
# w2c_model_path = '/home/zhangxin/work/workplace_python/DeepSentiment/data/word2vec_model/'
# w2c_model_path = 'data/model_w2v/mymodel'


#================================================================================
# train_data = ('neg', '/home/zhangxin/work/DeepSentiment/data/train_op/result_neg.txt')
# train_neu = ('neu', '/home/zhangxin/work/DeepSentiment/data/train_op/result_neu.txt')
# train_pos = ('pos', '/home/zhangxin/work/DeepSentiment/data/train_op/result_pos.txt')

# train_data = [('neg', '/home/zhangxin/work/DeepSentiment/data/train_op/result_neg.txt'),
#               ('neu', '/home/zhangxin/work/DeepSentiment/data/train_op/result_neu.txt'),
#               ('pos', '/home/zhangxin/work/DeepSentiment/data/train_op/result_pos.txt')]

# file_parent = '/home/zhangxin/work/workplace_python/DeepNaturalLanguageProcessing/DeepNLP/data'
# file_neg = '/home/zhangxin/work/workplace_python/DeepNaturalLanguageProcessing/DeepNLP/data/test3.txt'
# file_pos = '/home/zhangxin/work/workplace_python/DeepNaturalLanguageProcessing/DeepNLP/data/test2.txt'
# w2c_model_path = '/home/zhangxin/work/workplace_python/DeepNaturalLanguageProcessing/DeepNLP/word2vecmodel/mymodel'

# input_txt = '/Users/li/workshop/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data/input/myInput.txt'
# output_txt = '/Users/li/workshop/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data/input/myOutput.txt'
# stopword = '/Users/li/workshop/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data/stopword.txt'

# data_process_result = '/Users/li/workshop/DataSet/sentiment/tagging/result.txt'

# train_data = ('neg', '/Users/li/workshop/DataSet/sentiment/train_op/result_neg.txt')
# train_neu = ('neu', '/Users/li/workshop/DataSet/sentiment/train_op/result_neu.txt')
# train_pos = ('pos', '/Users/li/workshop/DataSet/sentiment/train_op/result_pos.txt')
#
# train_data = [('neg', '/Users/li/workshop/DataSet/sentiment/train_op/result_neg.txt'),
#               ('neu', '/Users/li/workshop/DataSet/sentiment/train_op/result_neu.txt'),
#               ('pos', '/Users/li/workshop/DataSet/sentiment/train_op/result_pos.txt')]

# file_parent = '/Users/li/workshop/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data'
# file_neg = '/Users/li/workshop/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data/test3.txt'
# file_pos = '/Users/li/workshop/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/data/test2.txt'
# w2c_model_path = '/Users/li/workshop/MyRepository/DeepNaturalLanguageProcessing/DeepNLP/word2vecmodel/model'
# w2c_model_path = '/Users/li/workshop/MyRepository/stock_industry_sentiment_analysis/data_warehouse/word2vec_model/w2cmodel2'
w2c_model_path = '/home/zhangxin/work/workplace_python/stock_industry_sentiment_analysis/data_warehouse/word2vec_model/w2cmodel'

# w2v模型的参数
n_dim = 200
min_count = 1
num_classes = 3


# pos_file_path = '/Users/li/workshop/DataSet/sentiment/train/result_pos.txt'
# neg_file_path = '/Users/li/workshop/DataSet/sentiment/train/result_neg.txt'
# neu_file_path = '/Users/li/workshop/DataSet/sentiment/train/result_neu.txt'
#
pos_file_path = '/home/zhangxin/work/workplace_python/DeepSentiment/data/train/result_pos.txt'
neg_file_path = '/home/zhangxin/work/workplace_python/DeepSentiment/data/train/result_neg.txt'
neu_file_path = '/home/zhangxin/work/workplace_python/DeepSentiment/data/train/result_neu.txt'


# 预测
model_rnn_path = '/home/zhangxin/work/workplace_python/stock_industry_sentiment_analysis' \
                 '/data_warehouse/classify_model/model_rnn/rnn_model'
# model_rnn_path = "/Users/li/workshop/MyRepository/stock_industry_sentiment_analysis/" \
#                  "data_warehouse/classify_model/model_rnn/rnn_model"
rnn_model_log = "/Users/li/workshop/MyRepository/stock_industry_sentiment_analysis/" \
                 "data_warehouse/classify_model/model_rnn/rnn_model_log"
predict_parent_file = '/home/zhangxin/work/workplace_python/DeepSentiment/DeepNaturalLanguageProcessing/' \
                      'DeepNLP/sentiment_analysis_zh/data/text_predict'
# predict_parent_file = '/Users/li/workshop/StanfordNLP/predict_test'


# 语义规则模型

# path_dit = {
#     'path_to_jar': u"/home/zhangxin/work/stanford/jars/stanford-parser.jar",
#     'path_to_models_jar': u"/home/zhangxin/work/stanford/jars/stanford-parser-3.6.0-models.jar",
#     # 'model_path': u"/home/zhangxin/work/stanford/jars/edu/chinesePCFG.ser.gz"
#     'model_path': u"/home/zhangxin/work/stanford/jars/edu/chineseFactored.ser.gz"
# }
path_dit = {
    'path_to_jar': u"/Users/li/workshop/StanfordNLP/stanford/jars/stanford-parser.jar",
    'path_to_models_jar': u"/Users/li/workshop/StanfordNLP/stanford/jars/stanford-parser-3.6.0-models.jar",
    'model_path': u"/Users/li/workshop/StanfordNLP/stanford/jars/edu/chinesePCFG.ser.gz"
}

corpus_path_dic = {
    'd_path': "/Users/li/workshop/StanfordNLP/stanfordcorpus/程度副词_datatang.txt",
    's_path': "/Users/li/workshop/StanfordNLP/stanfordcorpus/senti.txt",
    'f_path': "/Users/li/workshop/StanfordNLP/stanfordcorpus/fou.txt",
    'b_path': "/Users/li/workshop/StanfordNLP/stanfordcorpus/but.txt",
    'e_path': "/Users/li/workshop/StanfordNLP/stanfordcorpus/eng.txt"
}
# ================================================================================

