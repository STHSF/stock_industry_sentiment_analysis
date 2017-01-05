# coding=utf-8

import logging
import numpy as np
from data_prepare import corpus, data_processing
from gensim.models import Word2Vec
from tensorflow.contrib.learn.python.learn.datasets import base
from sentiment_polarity.word2vec_model import doc2vec_gensim_train
# from sentiment_polarity.data_processing
import globe
import re

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def _data_read(pos_file_path, neg_file_path, neu_file_path, w2c_model_path):
    """read data and word2vec model from file path, 并构造文本向量
    Args:
        pos_file_path: Positive file path.
        neg_file_path: Negative file path.
        w2c_model_path: word2vec model path
    Returns:
        A list contains train_op and test data vectors with labels.
    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pos_data = data_processing.read_source_data(pos_file_path)
    neg_data = data_processing.read_source_data(neg_file_path)
    neu_data = data_processing.read_source_data(neu_file_path)

    res = data_processing.data_split(pos_data, neu_data, neg_data)
    # tmp = data_processing.read_data(pos_file_path, neg_file_path)
    # res = data_processing.data_split(tmp[0], tmp[1])
    (train_data, test_data, train_labels, test_labels) = (res[0], res[1], res[2], res[3])

    # print train_labels[0]
    train_data = data_processing.text_clean(train_data)
    test_data = data_processing.text_clean(test_data)

    # 词向量的维度
    n_dim = globe.n_dim
    doc_vectors = []
    try:
        # load word2vec model from model path
        word2vec_model = Word2Vec.load(w2c_model_path)
        # 生成文本向量空间
        doc_vectors = doc2vec_gensim_train.doc_vectors(train_data, test_data, n_dim, word2vec_model)
    except IOError:
        pass

    train_data_vectors = doc_vectors[0]
    # print train_data_vectors.shape
    test_data_vectors = doc_vectors[1]
    # print test_data_vectors.shape

    return train_data_vectors, train_labels, test_data_vectors, test_labels


# def _read32(bytestream):
#     dt = np.dtype(np.uint32).newbyteorder('>')
#     return np.frombuffer(bytestream.read(4), dtype=dt)[0]


# def extract_images(filename):
#     """Extract the images into a 4D uint8 numpy array [index, y, x, depth]."""
#     with open(filename, 'rb') as bytestream:
#         num_images = _read32(bytestream)
#         rows = _read32(bytestream)
#         cols = _read32(bytestream)
#         buf = bytestream.read(rows * cols * num_images)
#         data = np.frombuffer(buf, dtype=np.uint8)
#         data = data.reshape(num_images, rows, cols, 1)
#     return data


def dense_to_one_hot(labels_dense, num_classes):
    """Convert class labels from scalars to one-hot vectors."""
    # print labels_dense.dtype
    num_labels = labels_dense.shape[0]
    index_offset = np.arange(num_labels) * num_classes
    labels_one_hot = np.zeros((num_labels, num_classes))
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
    return labels_one_hot


def extract_labels(labels, one_hot=False, num_classes=globe.num_classes):
    """Extract the labels into a 1D uint8 numpy array [index]."""
    # print labels.shape
    if one_hot:
        return dense_to_one_hot(labels.astype(np.uint8), num_classes)
    return labels


class DataSet(object):
    """Construct a DataSet.
    Attributes:
        data: text vectors
        labels: labels of every data
    """
    def __init__(self, data, labels):
        """inits DataSet.
        """
        self._data = data
        self._labels = labels
        self._epochs_completed = 0
        self._index_in_epoch = 0
        self._num_examples = data.shape[0]
        # 数据归一化

    @property
    def length(self):
        return self.length

    @property
    def data(self):
        return self._data

    @property
    def labels(self):
        return self._labels

    @property
    def num_examples(self):
        return self._num_examples

    @property
    def epochs_completed(self):
        return self._epochs_completed

    def next_batch(self, batch_size):
        """Return the next `batch_size` examples from this data set."""
        start = self._index_in_epoch
        self._index_in_epoch += batch_size
        if self._index_in_epoch > self._num_examples:
            # Finished epoch
            self._epochs_completed += 1
            # Shuffle the data
            perm = np.arange(self._num_examples)
            np.random.shuffle(perm)
            self._data = self._data[perm]
            self._labels = self._labels[perm]
            # Start next epoch
            start = 0
            self._index_in_epoch = batch_size
            assert batch_size <= self._num_examples
        end = self._index_in_epoch
        return self._data[start:end], self._labels[start:end]

    def next_batch_data(self, batch_size):
        """Return the next `batch_size` examples from this data set."""
        start = self._index_in_epoch
        self._index_in_epoch += batch_size
        if self._index_in_epoch > self._num_examples:
            # Finished epoch
            self._epochs_completed += 1
            # Shuffle the data
            perm = np.arange(self._num_examples)
            np.random.shuffle(perm)
            self._data = self._data[perm]
            # self._labels = self._labels[perm]
            # Start next epoch
            start = 0
            self._index_in_epoch = batch_size
            assert batch_size <= self._num_examples
        end = self._index_in_epoch
        return self._data[start:end]  # , self._labels[start:end]


def read_data_sets():

    # 读入数据
    pos_file_path = globe.pos_file_path
    neg_file_path = globe.neg_file_path
    neu_file_path = globe.neu_file_path
    w2c_model_path = globe.w2c_model_path

    raw_data = _data_read(pos_file_path, neg_file_path, neu_file_path, w2c_model_path)

    train_data = raw_data[0]
    # train_label = np.reshape(raw_data[1], (raw_data[1].shape[0],))
    # print train_label.shape
    train_labels = extract_labels(raw_data[1], one_hot=True)
    # for l in train_labels:
    #     print 'L ',l

    test_data = raw_data[2]
    # print test_data.shape
    # test_label = np.reshape(raw_data[3], (raw_data[1].shape[0], 1))
    test_labels = extract_labels(raw_data[3], one_hot=True)
    # print train_label.shape

    validation_size = 500
    validation_data = train_data[:validation_size]
    validation_labels = train_labels[:validation_size]
    train_data = train_data[validation_size:]
    train_labels = train_labels[validation_size:]

    train = DataSet(train_data, train_labels)
    # print train_op.raw_data[0], train_op.labels[0]
    validation = DataSet(validation_data, validation_labels)
    test = DataSet(test_data, test_labels)

    return base.Datasets(train=train, validation=validation, test=test)


def read_data_sets_predict():

    # 读入数据,并切词\去停处理
    predict_parent_file = globe.predict_parent_file
    file_seg = corpus.sentence(predict_parent_file)

    # 构建word2vec词向量
    w2c_model_path = globe.w2c_model_path

    text_vectors = {}
    try:
        word2vec_model = Word2Vec.load(w2c_model_path)

        for title in file_seg.keys():
            # print '【标题】', title
            # print '【正文】', file_seg[title]
            doc = file_seg[title]
            doc_vec = doc2vec_gensim_train.doc_vecs_zx(doc, word2vec_model)
            # text_vectors.append(doc_vec)
            text_vectors[title] = doc_vec
    except IOError:
        pass

    return text_vectors

# def load_data():
#     return read_data_sets()

if __name__ == '__main__':
    # read_data_sets()
    data = read_data_sets_predict()
    for title in data.keys():
        batch_xs = data[title]
        print title


