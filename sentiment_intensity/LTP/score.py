#!/usr/bin/env python
# encoding: utf-8
# -*- coding:utf-8 -*-
# -------------------------------------------
# 功能：基于规则计算情感值得分 _ 规则参考于兰秋军
# Author: zx
# Software: PyCharm Community Edition
# File: score.py
# Time: 16-12-8 下午2:09
# -------------------------------------------


def score(relation, D, S, P):
    relate = relation.relation
    relate_score = {
        "ADV": __adv(relation, D, S),
        "ATT": __att(relation, S, P),
        "COO": __coo(relation, S),
        "SBV": __sbv(relation, S),
        "VOB": __vob(relation, S),
        "CMP": __cmp(relation, S)
    }

    return relate_score.get(relate, 0)


def __adv(relation, D, S):
    pos_mw = relation.pos_mw
    pos_cw = relation.pos_cw

    if ((relation.pos_mw == "d" and relation.pos_cw.__eq__("v")) or (
                    relation.pos_mw == "d" and relation.pos_cw.__eq__("v"))) and relation.dd_mw:
        return D.get(relation.mw, 1) * S.get(relation.cw, 1)
    elif ((pos_mw == "d" and pos_cw == "v") or (pos_mw == "d" and pos_cw == "a")) and relation.nd_mw:
        return -S.get(relation.cw)
    elif (pos_mw == "nt" and pos_cw == "v") or (pos_mw == "p" and pos_cw == "v"):
        return S.get(relation.cw, 1)
    elif pos_mw == "a" and pos_cw == "v":
        return 0.5 * S.get(relation.mw, 1) + S.get(relation.cw, 1)
    elif pos_mw == "v" and pos_cw == "v":
        return S.get(relation.mw, 1) + S.get(relation.cw, 1)

    return 0


def __att(relation, S, P):
    pos_mw = relation.pos_mw
    pos_cw = relation.pos_cw

    if (pos_mw == "r" and pos_cw == "n") or (pos_mw == "m" and pos_cw == "n") or (pos_mw == "q" and pos_cw == "n"):
        return S.get(relation.cw, 1)
    elif pos_mw == "n" and pos_cw == "n":
        return S.get(relation.mw, 1) + S.get(relation.cw, 1)
    elif (pos_mw == "v" and pos_cw == "n") or (pos_mw == "a" and pos_cw == "n"):
        return abs(S.get(relation.mw, 1)) * P.get(relation.cw, -1)


def __coo(relation, S):
    return S.get(relation.mw, 1) + S.get(relation.cw, 1)


def __sbv(relation, S):
    pos_mw = relation.pos_mw
    pos_cw = relation.pos_cw

    if (pos_mw == "r" and pos_cw == "v") or (pos_mw == "nh" and pos_cw == "v") or (pos_mw == "ns" and pos_cw == "v"):
        return S.get(relation.cw, 1)
    elif pos_mw == "v" and pos_cw == "v":
        return S.get(relation.mw, 1) + S.get(relation.cw, 1)
    elif (pos_mw == "n" and pos_cw == "v") or (pos_mw == "n" and pos_cw == "a"):
        return S.get(relation.mw, 1) + 0.5 * S.get(relation.cw, 1)


def __vob(relation, S):
    pos_mw = relation.pos_mw
    pos_cw = relation.pos_cw

    if (pos_mw == "r" and pos_cw == "v") or (pos_mw == "m" and pos_cw == "v") or (pos_mw == "q" and pos_cw == "v"):
        return S.get(relation.cw, 1)
    elif pos_mw == "v" and pos_cw == "v":
        return S.get(relation.mw, 1) + S.get(relation.cw, 1)
    elif (pos_mw == "n" and pos_cw == "v") or (pos_mw == "a" and pos_cw == "v"):
        return 0.5 * S.get(relation.mw, 1) + S.get(relation.cw, 1)


def __cmp(relation, S):
    return S.get(relation.mw, 1) + S.get(relation.cw, 1)
