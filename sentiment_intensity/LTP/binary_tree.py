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

    # while len(relation_list) >0:

    T = []
    T_list = []
    for w in words:
        es = {}
        es_word = [w]   # 当前情感词的关联词集合

        sort_dict = {
            "VOB": 1,
            "ATT": 2,
            "ADV": 3,
            "VV": 4,
            "COO": 5,
            "SMP": 6,
            "SBV": 7,
            "CNJ": 8
        }


        # sort_dict = {
        #     "ATT": 1,
        #     "ADV": 2,
        #     "VV": 3,
        #     "COO": 4,
        #     "SMP": 5,
        #     "VOB": 6,
        #     "SBV": 7,
        #     "CNJ": 8
        # }

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


#实现相若晨论文中的二叉树构建
def btree_xrc(relation_list, words):
    """
    构建二叉树
    :param relation_list: 依存关系集合
    :param words: 原始词集合
    :return: 二叉树
    """
    #
    # for relation in relation_list:
    #     print relation.mw, " - ", relation.relation, " - ", relation.cw

    # while len(relation_list) >0:

    # relation_dict = {}
    # count = 1
    # for r in relation_list:
    #     relation_dict[count] = r
    #     count += 1
    # 直接用list的下标作为编号,,因此编号从0 开始

    # T = []
    T_list = []

    # 栈
    stack = []
    T = tree.Tree("root", ["", ""])
    T_word = []
    for w in words:

        if len(stack) == 0:
            print w
            stack.append(w)
        else:
            w0 = stack.pop()
            print w, w0
            for r in relation_list:
                if r.mw == w and r.cw == w0:
                    temp = tree.Tree(relation_list.index(r), [w, w0])
                    T_word.append([w, w0])


                    T = temp
                elif r.mw == w0 and r.cw == w:
                    temp = tree.Tree(relation_list.index(r), [w0, w])
                    T_word.append([w, w0])
                    T = temp

    T.draw()


# zx
def btree_zx(relation_list):
    """
    构建二叉树
    :param relation_list: 依存关系集合
    :param words: 原始词集合
    :return: 二叉树
    """

    # while len(relation_list) >0:

    # relation_dict = {}
    # count = 1
    # for r in relation_list:
    #     relation_dict[count] = r
    #     count += 1
    # 直接用list的下标作为编号,,因此编号从0 开始

    # 栈
    stack = []

    list_copy = []
    for r in relation_list:
        list_copy.append(r)

    T = tree.Tree("root", ["", ""])
    T_list = []
    T_word = []

    for n in range(len(relation_list)):
        r = relation_list.pop()

        mw = r.mw
        cw = r.cw

        id = list_copy.index(r)

        # 如果是并列关系: COO
        if r.relation == "COO":
            print "\n[COO]---"
            if not T_word.__contains__(mw) and not T_word.__contains__(cw):
                temp = creat_tree(mw, cw, r.relation, id)
                T_word.extend([mw, cw])
                T = temp
                T_list.append(T)
            elif T_word.__contains__(mw) and not T_word.__contains__(cw):
                print "[2]", mw, cw
                T_word.append(cw)

                temp = T
                T = tree.Tree(id, [temp, cw])
                T_list.append(T)
            elif not T_word.__contains__(mw) and T_word.__contains__(cw):
                print "[3]", mw, cw
                T_word.append(mw)

                temp = T
                T = tree.Tree(id, [mw, temp])
                T_list.append(T)
            else:
                print "[4]", mw, cw
                n1 = tree.Tree("n1", ["", ""])
                n2 = tree.Tree("n2", ["", ""])

                for t in T_list:
                    if t.leaves().__contains__(cw):
                        n1 = t
                    if t.leaves().__contains__(mw):
                        n2 = t
                T = tree.Tree(id, [n2, n1])
                T_list.append(T)
        else:
            print "\n[不是COO]---"
            if not T_word.__contains__(mw) and not T_word.__contains__(cw):
                print "[1]", mw, cw
                temp = creat_tree(mw, cw, r.relation, id)
                T_word.extend([mw, cw])
                T = temp
                T_list.append(T)
            elif T_word.__contains__(mw) and not T_word.__contains__(cw):
                print "[2]", mw, cw
                T_word.append(cw)

                temp = T
                T = tree.Tree(id, [temp, cw])
                T_list.append(T)
            elif not T_word.__contains__(mw) and T_word.__contains__(cw):
                print "[3]", mw, cw
                T_word.append(mw)
                temp = T
                T = tree.Tree(id, [mw, temp])
                T_list.append(T)
            else:
                print "[4]", mw, cw
                n1 = tree.Tree("n1", ["", ""])
                n2 = tree.Tree("n2", ["", ""])

                for t in T_list:
                    if t.leaves().__contains__(cw):
                        n1 = t
                    if t.leaves().__contains__(mw):
                        n2 = t
                T = tree.Tree(id, [n2, n1])
                T_list.append(T)


    T.draw()


def creat_tree(mw, cw, relation, id):

    if relation == "VOB":
        return tree.Tree(id, [cw, mw])
    # elif



#
# a = [1,2,3,4]
# b=[]
# for i in a:
#     b.append(i)
#
#
# for n in range(len(a)):
#     print n, a.pop()
#     print
#
#
#
# print b