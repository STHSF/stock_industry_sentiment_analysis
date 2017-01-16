#!/usr/bin/env python
# encoding: utf-8

# -------------------------------------------
# 功能：用于挑选 pos词 和 neg词
# Author: zx
# Software: PyCharm Community Edition
# File: main.py
# Time: 16-11-18 上午11:00
# -------------------------------------------
import sys

from PyQt4 import QtGui

import frame


def fram():
    # 显示主页面
    app = QtGui.QApplication(sys.argv)
    win = frame.Run_2_content_Form()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    fram()
