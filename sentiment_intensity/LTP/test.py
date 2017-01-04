#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: test.py
# Time: 16-12-8 下午2:40
# -------------------------------------------

# 耗时测试
# time_begin = time.time()
# text = "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族." \
#        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族." \
#        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族." \
#        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
#        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
#        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
#        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
#        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族" \
#        "今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族.今天的股票涨势挺好.我喜欢苹果.我讨厌小米和魅族"
# text_arr = text.split(".")
# result_list = []
# count = 1
# for t in text_arr:
#     print count, " ", t
#     count += 1
#     result = parser(t)
#     result_list.append(result)
#
# time_end = time.time()
# print "[句子个数] ", len(text_arr)
# print "[结果] ", len(result_list)
# print "[总耗时]", time_end - time_begin




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