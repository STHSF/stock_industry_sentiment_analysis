#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: tree.py
# Time: 16-12-22 下午2:43
# -------------------------------------------

import nltk.tree as tree


# 递归遍历
def test(t):
    if isinstance(t, str):
        print t
    else:
        for i in range(len(t)):
            test(t[len(t)-i-1])


# 非递归调用
def test_2(t):
    stack = []
    stack.append(t)

    current = ""
    while stack:
        current = stack.pop()

        if isinstance(current, tree.Tree):
            for i in range(len(current)):
                stack.append(current[i])

        elif isinstance(current, str):
            # print "[输出] ",current
            print current


if __name__ == "__main__":
    C = tree.Tree("C", ["E", "F"])
    B = tree.Tree("B", [C, "D"])
    M = tree.Tree("M", ["O", "P"])
    H = tree.Tree("H", [M, "N"])
    G = tree.Tree("G", ["X", "Y"])
    A = tree.Tree("A", [G, H])
    K = tree.Tree("K", ["L", "Q"])

    root = tree.Tree("Root", [A, B, K])


    print root[0]
    print root.height()
    print len(root)
    print type(root)

    import time

    begin = time.time()
    test(root)
    print time.time()-begin

    begin2 = time.time()
    test_2(root)
    print time.time()-begin2

    root.draw()
