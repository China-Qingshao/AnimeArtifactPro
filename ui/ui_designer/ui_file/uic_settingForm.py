# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingForm(object):
    def setupUi(self, settingForm):
        settingForm.setObjectName("settingForm")
        settingForm.resize(375, 442)
        settingForm.setMinimumSize(QtCore.QSize(375, 375))
        settingForm.setMaximumSize(QtCore.QSize(375, 500))
        self.gridLayout = QtWidgets.QGridLayout(settingForm)
        self.gridLayout.setContentsMargins(7, 7, 7, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(settingForm)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lblIDM = QtWidgets.QLabel(self.tab)
        self.lblIDM.setGeometry(QtCore.QRect(130, 170, 151, 41))
        self.lblIDM.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblIDM.setWordWrap(True)
        self.lblIDM.setObjectName("lblIDM")
        self.lblPlayerPot = QtWidgets.QLabel(self.tab)
        self.lblPlayerPot.setGeometry(QtCore.QRect(130, 60, 151, 41))
        self.lblPlayerPot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblPlayerPot.setWordWrap(True)
        self.lblPlayerPot.setObjectName("lblPlayerPot")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 61, 21))
        self.label_3.setObjectName("label_3")
        self.txtUserName = QtWidgets.QLineEdit(self.tab)
        self.txtUserName.setGeometry(QtCore.QRect(80, 10, 211, 21))
        self.txtUserName.setObjectName("txtUserName")
        self.btnTestPlayerVlc = QtWidgets.QPushButton(self.tab)
        self.btnTestPlayerVlc.setGeometry(QtCore.QRect(290, 110, 51, 23))
        self.btnTestPlayerVlc.setObjectName("btnTestPlayerVlc")
        self.btnChoosePlayerVlc = QtWidgets.QToolButton(self.tab)
        self.btnChoosePlayerVlc.setGeometry(QtCore.QRect(80, 110, 37, 21))
        self.btnChoosePlayerVlc.setObjectName("btnChoosePlayerVlc")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 255, 336, 111))
        self.groupBox.setObjectName("groupBox")
        self.checkClosingWarning = QtWidgets.QCheckBox(self.groupBox)
        self.checkClosingWarning.setGeometry(QtCore.QRect(10, 20, 101, 20))
        self.checkClosingWarning.setObjectName("checkClosingWarning")
        self.checkPlaySound = QtWidgets.QCheckBox(self.groupBox)
        self.checkPlaySound.setGeometry(QtCore.QRect(10, 50, 101, 20))
        self.checkPlaySound.setObjectName("checkPlaySound")
        self.checkCheckUpdate = QtWidgets.QCheckBox(self.groupBox)
        self.checkCheckUpdate.setGeometry(QtCore.QRect(10, 80, 101, 20))
        self.checkCheckUpdate.setObjectName("checkCheckUpdate")
        self.btnCheckUpdate = QtWidgets.QPushButton(self.groupBox)
        self.btnCheckUpdate.setGeometry(QtCore.QRect(110, 80, 81, 21))
        self.btnCheckUpdate.setObjectName("btnCheckUpdate")
        self.checkBrowserDecodeM3u = QtWidgets.QCheckBox(self.groupBox)
        self.checkBrowserDecodeM3u.setGeometry(QtCore.QRect(190, 20, 121, 20))
        self.checkBrowserDecodeM3u.setObjectName("checkBrowserDecodeM3u")
        self.checkBrowserDecodeAll = QtWidgets.QCheckBox(self.groupBox)
        self.checkBrowserDecodeAll.setGeometry(QtCore.QRect(190, 50, 121, 20))
        self.checkBrowserDecodeAll.setObjectName("checkBrowserDecodeAll")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 167, 41, 21))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 57, 41, 21))
        self.label_2.setObjectName("label_2")
        self.btnChooseIDM = QtWidgets.QToolButton(self.tab)
        self.btnChooseIDM.setGeometry(QtCore.QRect(80, 167, 37, 21))
        self.btnChooseIDM.setObjectName("btnChooseIDM")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 51, 21))
        self.label_6.setObjectName("label_6")
        self.btnFinished_1 = QtWidgets.QPushButton(self.tab)
        self.btnFinished_1.setGeometry(QtCore.QRect(272, 374, 75, 23))
        self.btnFinished_1.setObjectName("btnFinished_1")
        self.comboDefaultInterface = QtWidgets.QComboBox(self.tab)
        self.comboDefaultInterface.setGeometry(QtCore.QRect(90, 220, 91, 22))
        self.comboDefaultInterface.setObjectName("comboDefaultInterface")
        self.comboDefaultInterface.addItem("")
        self.comboDefaultInterface.addItem("")
        self.comboDefaultInterface.addItem("")
        self.comboDefaultInterface.addItem("")
        self.comboDefaultInterface.addItem("")
        self.btnTestPlayerPot = QtWidgets.QPushButton(self.tab)
        self.btnTestPlayerPot.setGeometry(QtCore.QRect(290, 57, 51, 23))
        self.btnTestPlayerPot.setObjectName("btnTestPlayerPot")
        self.btnTestIDM = QtWidgets.QPushButton(self.tab)
        self.btnTestIDM.setGeometry(QtCore.QRect(290, 167, 51, 23))
        self.btnTestIDM.setObjectName("btnTestIDM")
        self.btnChoosePlayerPot = QtWidgets.QToolButton(self.tab)
        self.btnChoosePlayerPot.setGeometry(QtCore.QRect(80, 57, 37, 21))
        self.btnChoosePlayerPot.setObjectName("btnChoosePlayerPot")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 10, 41, 21))
        self.label.setObjectName("label")
        self.lblPlayerVlc = QtWidgets.QLabel(self.tab)
        self.lblPlayerVlc.setGeometry(QtCore.QRect(130, 113, 151, 41))
        self.lblPlayerVlc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblPlayerVlc.setWordWrap(True)
        self.lblPlayerVlc.setObjectName("lblPlayerVlc")
        self.btnChangeBG = QtWidgets.QPushButton(self.tab)
        self.btnChangeBG.setGeometry(QtCore.QRect(266, 220, 75, 23))
        self.btnChangeBG.setObjectName("btnChangeBG")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(settingForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(settingForm)

    def retranslateUi(self, settingForm):
        _translate = QtCore.QCoreApplication.translate
        settingForm.setWindowTitle(_translate("settingForm", "设置"))
        self.lblIDM.setText(_translate("settingForm", "无"))
        self.lblPlayerPot.setText(_translate("settingForm", "无"))
        self.label_3.setText(_translate("settingForm", "备用播放器"))
        self.btnTestPlayerVlc.setText(_translate("settingForm", "测试"))
        self.btnChoosePlayerVlc.setText(_translate("settingForm", "..."))
        self.groupBox.setTitle(_translate("settingForm", "开关"))
        self.checkClosingWarning.setText(_translate("settingForm", "关闭窗口警告"))
        self.checkPlaySound.setText(_translate("settingForm", "播放音效"))
        self.checkCheckUpdate.setText(_translate("settingForm", "自动检查更新"))
        self.btnCheckUpdate.setText(_translate("settingForm", "点我手动检查"))
        self.checkBrowserDecodeM3u.setText(_translate("settingForm", "使用网页解析m3u8"))
        self.checkBrowserDecodeAll.setText(_translate("settingForm", "一律使用网页解析"))
        self.label_5.setText(_translate("settingForm", "下载器"))
        self.label_2.setText(_translate("settingForm", "播放器"))
        self.btnChooseIDM.setText(_translate("settingForm", "..."))
        self.label_6.setText(_translate("settingForm", "默认接口"))
        self.btnFinished_1.setText(_translate("settingForm", "完成"))
        self.comboDefaultInterface.setItemText(0, _translate("settingForm", "接口1"))
        self.comboDefaultInterface.setItemText(1, _translate("settingForm", "接口2"))
        self.comboDefaultInterface.setItemText(2, _translate("settingForm", "接口3"))
        self.comboDefaultInterface.setItemText(3, _translate("settingForm", "接口4"))
        self.comboDefaultInterface.setItemText(4, _translate("settingForm", "接口5"))
        self.btnTestPlayerPot.setText(_translate("settingForm", "测试"))
        self.btnTestIDM.setText(_translate("settingForm", "测试"))
        self.btnChoosePlayerPot.setText(_translate("settingForm", "..."))
        self.label.setText(_translate("settingForm", "用户名"))
        self.lblPlayerVlc.setText(_translate("settingForm", "无"))
        self.btnChangeBG.setText(_translate("settingForm", "切换背景图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("settingForm", "常规"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("settingForm", "其他"))
