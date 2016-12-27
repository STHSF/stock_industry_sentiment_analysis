#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# -------------------------------------------
# 功能：界面+主要逻辑
# Author: zx
# Software: PyCharm Community Edition
# File: frame.py
# Time: 16-11-18 上午11:17
# -------------------------------------------

from PyQt4 import QtCore, QtGui
import sys
import globe
from PyQt4.QtGui import QMessageBox
from functools import partial


reload(sys)
sys.setdefaultencoding('utf8')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Run_2_content_Form(QtGui.QMainWindow):
    def __init__(self):
        super(Run_2_content_Form, self).__init__()
        self.names = locals()

        # 获取类标
        self.qtext = QtCore.QStringList()
        for l in globe.labels:
            print l
            self.qtext.append(unicode(l))

        self.setup_ui(self)
        self.retranslate_ui(self)
        self.checkLisk = set()
        # self.search()

    def setup_ui(self, dialog):

        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(657, 853)

        # 类别标签
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))

        # 类别标签关键词框
        self.kek_word = QtGui.QComboBox(dialog)
        self.kek_word.setGeometry(QtCore.QRect(100, 30, 111, 31))
        self.kek_word.setObjectName(_fromUtf8("kek_word"))
        self.kek_word.addItems(self.qtext)

        # 状态栏 : 已选中 / 总计
        self.label_state = QtGui.QLabel(dialog)
        self.label_state.setGeometry(QtCore.QRect(20, 78, 81, 31))
        self.label_state.setObjectName(_fromUtf8("label_state"))

        self.label_state_text = QtGui.QLabel(dialog)
        self.label_state_text.setGeometry(QtCore.QRect(100, 78, 160, 31))
        self.label_state_text.setObjectName(_fromUtf8("label_state_text"))

        self.label_state_page = QtGui.QLabel(dialog)
        self.label_state_page.setGeometry(QtCore.QRect(260, 78, 140, 31))
        self.label_state_page.setObjectName(_fromUtf8("label_state_page"))

        self.label_state_label = QtGui.QLabel(dialog)
        self.label_state_label.setGeometry(QtCore.QRect(420, 78, 160, 31))
        self.label_state_label.setObjectName(_fromUtf8("label_state_label"))

        self.label_state_reset = QtGui.QLabel(dialog)
        self.label_state_reset.setGeometry(QtCore.QRect(570, 78, 65, 31))
        self.label_state_reset.setObjectName(_fromUtf8("label_state_reset"))

        # 相关新闻
        self.label_3 = QtGui.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        # 复选框
        a = 127
        for n in range(24):
            self.names['cb%s' % n] = QtGui.QCheckBox('Show title', self)
            self.names['cb%s' % n].setGeometry(QtCore.QRect(98, a, 500, 20))
            self.names['cb%s' % n].stateChanged.connect(partial(self.changeTitle, 'cb%s' % n))
            a += 26

        # cb.toggle()    # 加上则默认已选

        # 跳转按钮
        self.button_search = QtGui.QPushButton(dialog)
        self.button_search.setGeometry(QtCore.QRect(230, 30, 60, 31))
        self.button_search.setObjectName(_fromUtf8("button_index"))

        # 上一篇
        self.button_last = QtGui.QPushButton(dialog)
        self.button_last.setGeometry(QtCore.QRect(120, 770, 75, 45))
        self.button_last.setObjectName(_fromUtf8("button_last"))

        # 下一篇
        self.Button_next = QtGui.QPushButton(dialog)
        self.Button_next.setGeometry(QtCore.QRect(230, 770, 75, 45))
        self.Button_next.setObjectName(_fromUtf8("Button_next"))

        # 写出
        self.button_writer_out = QtGui.QPushButton(dialog)
        self.button_writer_out.setGeometry(QtCore.QRect(350, 770, 75, 45))
        self.button_writer_out.setObjectName(_fromUtf8("button_writer_out"))

        # 无效删除
        self.button_reset = QtGui.QPushButton(dialog)
        self.button_reset.setGeometry(QtCore.QRect(460, 770, 75, 45))
        self.button_reset.setObjectName(_fromUtf8("button_reset"))

        # self.retranslate_ui(dialog)
        QtCore.QObject.connect(self.button_last, QtCore.SIGNAL(_fromUtf8("clicked()")), self.last_event)
        QtCore.QObject.connect(self.Button_next, QtCore.SIGNAL(_fromUtf8("clicked()")), self.next_event)
        QtCore.QObject.connect(self.button_search, QtCore.SIGNAL(_fromUtf8("clicked()")), self.search)
        QtCore.QObject.connect(self.button_writer_out, QtCore.SIGNAL(_fromUtf8("clicked()")), self.write_out)
        QtCore.QObject.connect(self.button_reset, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reset)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "分类数据人工标注系统", None))
        self.label.setText(_translate("dialog", "类别名称", None))
        self.label_3.setText(_translate("dialog", "相关新闻", None))
        self.label_state.setText(_translate("dialog", "状  态  栏", None))
        self.button_last.setText(_translate("dialog", "上一页", None))
        self.Button_next.setText(_translate("dialog", "下一页", None))
        self.button_writer_out.setText(_translate("dialog", "写出", None))
        self.button_reset.setText(_translate("dialog", "全部重置", None))
        self.button_search.setText(_translate("dialog", "搜一下", None))

    def changeTitle(self, cb):
        state = self.names[cb].checkState()
        if state == QtCore.Qt.Checked:
            self.checkLisk.add(self.names[cb].text())
            # 更新状态栏
            self.label_state_text.setText(
                unicode("[已选/总数]  ") + str(len(self.checkLisk)) + " / " + str(len(globe.docs)))

        else:
            try:
                self.checkLisk.remove(self.names[cb].text())
            except Exception, ex:
                print "[没找到] ", self.names[cb].text()

            # 更新状态栏
            self.label_state_text.setText(
                unicode("[已选/总数]  ") + str(len(self.checkLisk)) + " / " + str(len(globe.docs)))

    def search(self):

        # 初始化
        self.checkLisk.clear()
        globe.docs = []
        globe.current_index = 0

        key_word = self.kek_word.currentText()
        globe.current_label = key_word

        word = self.get_dict(key_word)

        for r in word.keys():
            title = r
            globe.docs.append(title)

        # 填充复选框
        if len(globe.docs) > 0:
            for i in range(24):
                cb = "cb" + str(i)
                self.names[cb].setText(globe.docs[i])
                state = self.names[cb].checkState()
                if state == QtCore.Qt.Checked:
                    self.names[cb].toggle()
        else:
            self.label_state_text.setText("无数据")

        # 更新状态栏
        self.label_state_text.setText(unicode("[已选/总数]  ") + str(len(self.checkLisk)) + " / " + str(len(globe.docs)))
        self.label_state_page.setText(
            unicode("[当页/总页]  ") + str(globe.current_index / 24 + 1) + " / " + str(len(globe.docs) / 24))
        self.label_state_label.setText(unicode("[当前类别]  ") + globe.current_label)

    # 下一个事件
    def next_event(self):

        if globe.current_index < len(globe.docs):

            globe.current_index += 24

            # 填充复选框
            for i in range(24):
                cb = "cb" + str(i)
                self.names[cb].setText(globe.docs[i + globe.current_index])
                state = self.names[cb].checkState()
                if state == QtCore.Qt.Checked:
                    self.names[cb].toggle()

            self.label_state_text.setText(
                unicode("[已选/总数]  ") + str(len(self.checkLisk)) + " / " + str(len(globe.docs)))
            self.label_state_page.setText(
                unicode("[当页/总页]  ") + str(globe.current_index / 24 + 1) + " / " + str(len(globe.docs) / 24))
            self.label_state_label.setText(unicode("[当前类别]  ") + globe.current_label)
        else:
            self.label_state_reset.setText(unicode("后无数据"))

    # 上一个事件
    def last_event(self):

        if globe.current_index >= 24:

            globe.current_index -= 24

            # 填充复选框
            for i in range(24):
                cb = "cb" + str(i)
                self.names[cb].setText(globe.docs[i + globe.current_index])
                state = self.names[cb].checkState()
                if state == QtCore.Qt.Checked:
                    self.names[cb].toggle()

            self.label_state_text.setText(
                unicode("[已选/总数]  ") + str(len(self.checkLisk)) + " / " + str(len(globe.docs)))
            self.label_state_page.setText(
                unicode("[当页/总页]  ") + str(globe.current_index / 24 + 1) + " / " + str(len(globe.docs) / 24))
            self.label_state_label.setText(unicode("[当前类别]  ") + globe.current_label)
        else:
            self.label_state_reset.setText(unicode("前无数据"))

    # 写出到本地文件
    def write_out(self):
        self.label_state_reset.setText(unicode("正在写"))
        writer = open(globe.output + self.kek_word.currentText() + "_" + str(len(self.checkLisk)) + ".txt", "wb")
        for doc in self.checkLisk:
            writer.write(unicode(doc) + "\n")
        writer.flush()
        writer.close()
        self.label_state_reset.setText(unicode("已写出"))

    # 一键重置
    def reset(self):
        customMsgBox = QMessageBox(self)
        customMsgBox.setWindowTitle("Custom message box")

        okButton = customMsgBox.addButton(unicode("确定"), QMessageBox.ActionRole)
        cancelButton = customMsgBox.addButton(unicode("取消"), QMessageBox.ActionRole)

        customMsgBox.setText(unicode("确定重置么？"))
        customMsgBox.exec_()

        button = customMsgBox.clickedButton()
        if button == okButton:
            self.checkLisk.clear()

            # 填充复选框
            for i in range(24):
                cb = "cb" + str(i)
                state = self.names[cb].checkState()
                if state == QtCore.Qt.Checked:
                    self.names[cb].toggle()

            # 更新状态栏
            # self.label_state_text.setText("0 / " + str(len(globe.docs)))
            self.label_state_text.setText(unicode("[已选/总数]  ") + str("0 / " + str(len(globe.docs))))
            self.label_state_reset.setText(unicode("已重置"))
        elif button == cancelButton:
            self.label_state_reset.setText(unicode("已取消"))

    def get_dict(self, flag):

        zhi = ""
        if flag == "pos":
            zhi = '/home/zhangxin/文档/市场情绪分析/情感词典/服务器/zhi_pos_2.txt'
        elif flag =="neg":
            zhi = '/home/zhangxin/文档/市场情绪分析/情感词典/服务器/zhi_neg_2.txt'

        word = {}
        for z in open(zhi):
            z = z.decode("utf-8")
            z = z.split("\t")
            word[z[0]] = word.get(z[0], 0) + int(z[1])

        return word
