#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：
# Author: zx
# Software: PyCharm Community Edition
# File: multi.py
# Time: 16-12-22 下午4:20
# -------------------------------------------
import multiprocessing
import time


def func(msg):
  for i in xrange(3):
    print msg
    time.sleep(1)   # 休眠1秒

# 单进程
def one_process():
    p = multiprocessing.Process(target=func, args=("hello",))
    p.start()
    p.join()
    print "Sub-process done."


# 线程池
def pool_process():
    pool = multiprocessing.Pool(processes=4)
    for i in xrange(10):
        msg = "hello %d" % (i)
        pool.apply_async(func, (msg,))
    pool.close()
    pool.join()
    print "Sub-process(es) done."


#使用Pool，并需要关注结果
def result_process():
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(10):
        msg = "hello %d" % (i)
        result.append(pool.apply_async(func, (msg,)))
    pool.close()
    pool.join()
    for res in result:
        print res.get()
    print "Sub-process(es) done."

if __name__ == "__main__":
    pool_process()