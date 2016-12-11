#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：依存关系类, 即一条依存弧连接的两个成分词
# Author: zx
# Software: PyCharm Community Edition
# File: relation.py
# Time: 16-12-8 下午4:48
# -------------------------------------------


# 依存关系类
class Relation:
    def __init__(self, mw, cw, relation, pos_mw, pos_cw, id_mw, id_cw, dd_mw=False, dd_cw=False, nd_mw=False,
                 nd_cw=False):
        self.mw = mw  # 修饰词
        self.cw = cw  # 支配词
        self.relation = relation
        self.pos_mw = pos_mw
        self.pos_cw = pos_cw
        self.id_mw = id_mw
        self.id_cw = id_cw

        self.dd_mw = dd_mw
        self.dd_cw = dd_cw
        self.nd_mw = nd_mw
        self.nd_cw = nd_cw

        self.is_senti_mw = False
        self.is_senti_cw = False
