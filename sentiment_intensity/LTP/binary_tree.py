#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：根据依存关系构建二叉树
# Author: zx
# Software: PyCharm Community Edition
# File: binary_tree.py
# Time: 16-12-9 上午9:24
# -------------------------------------------
import nltk.tree as tree


def btree(relation_list, words):
    """
    构建二叉树
    :param relation_list: 依存关系集合
    :param words: 情感词词集合
    :return: 二叉树
    """
    #
    # for relation in relation_list:
    #     print relation.mw, " - ", relation.relation, " - ", relation.cw
    T = []
    # while len(relation_list) >0:
    for w in words:
        es = {}
        es_word = [w]   # 当前情感词的关联词集合
        sort_dict = {
            "ATT": 1,
            "ADV": 2,
            "VV": 3,
            "COO": 4,
            "SMP": 5,
            "VOB": 6,
            "SBV": 7,
            "CNJ": 8
        }

        # 查找情感词关联的依存关系
        for relation in relation_list:
            if es_word.__contains__(relation.mw) or es_word.__contains__(relation.cw):

                es_word.append(relation.mw)
                es_word.append(relation.cw)

                print relation.mw, " - ", relation.relation, " - ", relation.cw
                es[relation] = sort_dict[relation.relation]

                # relation_list.remove(relation)

        # 对es中的依存关系进行排序得到rs
        es_sort = sorted(es.iteritems(), key=lambda d: d[1], reverse=False)

        rs = []
        for e in es_sort:
            rs.append(e[0])

        print "-----------------"
        for r in rs:
            print r.mw, " - ", r.relation, " - ", r.cw

        # 剔除rs 中的CNJ得到rs1

        # 开始遍历建树
        T1 = tree.Tree("root", ["", ""])  # 某个情感词关联的所有依存
        T1_word = []
        T1_list = []   # 子树集合

        for r in rs:
            name = r.relation
            w1 = r.cw
            w2 = r.mw

            if not T1_word.__contains__(w1) and not T1_word.__contains__(w2):
                print "[1]",w1,w2
                n1 = w1
                n2 = w2
                T1_word.append(w1)
                T1_word.append(w2)

                print T1.leaves()[1].__len__()
                if T1.leaves()[0].__len__() == 0:
                    T1 = tree.Tree(name, [n2, n1])
                    T1_list.append(T1)
                else:
                    temp = tree.Tree(name, [n2, n1])
                    T1_list.append(temp)
                    # T1 = tree.Tree(name, [T1, temp])

            elif T1_word.__contains__(w1) and not T1_word.__contains__(w2):
                print "[2]", w1, w2
                T1_word.append(w2)
                n1 = T1
                n2 = w2

                T1 = tree.Tree(name, [n2, n1])

            elif T1_word.__contains__(w2) and not T1_word.__contains__(w1):
                print "[3]", w1, w2
                n1 = "RIGHT"
                n2 = w2
                T1_word.append(w1)
            else:
                print "[4]", w1, w2
                n1 = tree.Tree("n1", ["", ""])
                n2 = tree.Tree("n2", ["", ""])

                for t in T1_list:
                    if t.leaves().__contains__(w1):
                        n1 = t
                    if t.leaves().__contains__(w2):
                        n2 = t

                T1 = tree.Tree(name, [n2, n1])

#
        T1.draw()
#
# tree1 = tree.Tree('NP', ['the', 'rabbit'])
# print(tree1)
#
# tree2 = tree.Tree('root', [tree1, 'test'])
# tree2.insert(2, ['good'])
# tree2.append(tree1)
# tree2.append(["OK"])
# tree2.set_label("Zhangxin")
#
# tree3 = tree2.subtrees()
#
# tree4 = tree.Tree(u"测试", ["", ""])
# tree4.set_label("ceshi")
# tree4.insert(0, tree1)
# tree2.append(tree4)
#
#
# print tree3
# for t in tree3:
#     print t
# # tree3.draw()
# tree2.draw()
#
# zishu = tree2.leaves()
# for l in zishu:
#     print l


# for r in rs:
#     name = r.relation
#     w1 = r.cw
#     w2 = r.mw
#
#     # n = tree.Tree(name, ["", ""])
#     # T1.append(n)
#
#     n1 = ""
#     n2 = ""
#
#     if not T1_word.__contains__(w1) and not T1_word.__contains__(w2):
#         print "[1]", w1, w2
#         n1 = w2
#         n2 = w1
#         T1_word.append(w1)
#         T1_word.append(w2)
#     elif T1_word.__contains__(w1) and not T1_word.__contains__(w2):
#         print "[2]", w1, w2
#         n1 = w2
#         T1_word.append(w2)
#         n2 = "LEFT"
#     elif T1_word.__contains__(w2) and not T1_word.__contains__(w1):
#         print "[3]", w1, w2
#         n1 = "RIGHT"
#         n2 = w1
#         T1_word.append(w1)
#     # else:
#
#     if n1 == "RIGHT":
#         T1.insert(1, T1.__getitem__(1))
#
#     else:
#         T1.insert(1, n1)
#     if n2 == "LEFT":
#         T1.insert(0, T1.__getitem__(0))
#     else:
#         T1.insert(0, n2)