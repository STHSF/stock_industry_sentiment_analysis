#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: time.py
# Time: 16-11-24 下午3:06
# -------------------------------------------
import time


# 时间转时间戳
def time_stamp(time_give):
    old_time_date = time.strptime(time_give, "%Y-%m-%d %H:%M:%S")

    old_time_date_stamp = time.mktime(old_time_date)

    return int(old_time_date_stamp * 1000)


# 时间戳转时间
def stamp_2_time(stamp):
    x = time.localtime(int(stamp) / 1000)
    y = time.strftime('%Y-%m-%d %H:%M:%S', x)
    z = time.strftime('%Y-%m-%d %H:%M', x)

    return y
