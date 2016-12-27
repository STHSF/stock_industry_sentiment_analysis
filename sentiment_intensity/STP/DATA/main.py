#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：用于从新闻库中抽取合适的行业语料,补充分类语料库
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 16-11-18 上午11:00
# -------------------------------------------
from PyQt4 import QtCore, QtGui
import sys
import frame

def fram():
    # 显示主页面
    app = QtGui.QApplication(sys.argv)
    win = frame.Run_2_content_Form()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    fram()
