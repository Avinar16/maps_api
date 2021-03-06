# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 825)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1045, 825))
        MainWindow.setMaximumSize(QtCore.QSize(1045, 825))
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet("background-color: rgb(90, 90, 90)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(430, 10, 600, 450))
        self.Image.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"                                  border-style: outset;\n"
"                                  border-color: rgb(0, 0, 0);\n"
"                                  border-width: 5px;\n"
"                                  border-radius:15px;")
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.LL = QtWidgets.QLineEdit(self.centralwidget)
        self.LL.setGeometry(QtCore.QRect(10, 50, 391, 20))
        self.LL.setMouseTracking(True)
        self.LL.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LL.setObjectName("LL")
        self._label_cords = QtWidgets.QLabel(self.centralwidget)
        self._label_cords.setGeometry(QtCore.QRect(10, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("SamsungOneUI Medium Condensed")
        font.setPointSize(14)
        self._label_cords.setFont(font)
        self._label_cords.setStyleSheet("color: rgb(255, 255, 255);")
        self._label_cords.setObjectName("_label_cords")
        self._label_ms = QtWidgets.QLabel(self.centralwidget)
        self._label_ms.setGeometry(QtCore.QRect(10, 90, 131, 16))
        font = QtGui.QFont()
        font.setFamily("SamsungOneUI Medium Condensed")
        font.setPointSize(14)
        self._label_ms.setFont(font)
        self._label_ms.setStyleSheet("color: rgb(255, 255, 255);")
        self._label_ms.setObjectName("_label_ms")
        self.Spn = QtWidgets.QLineEdit(self.centralwidget)
        self.Spn.setGeometry(QtCore.QRect(10, 120, 391, 20))
        self.Spn.setMouseTracking(True)
        self.Spn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Spn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Spn.setFrame(True)
        self.Spn.setObjectName("Spn")
        self._label_mapview = QtWidgets.QLabel(self.centralwidget)
        self._label_mapview.setGeometry(QtCore.QRect(10, 160, 131, 16))
        font = QtGui.QFont()
        font.setFamily("SamsungOneUI Medium Condensed")
        font.setPointSize(14)
        self._label_mapview.setFont(font)
        self._label_mapview.setStyleSheet("color: rgb(255, 255, 255);")
        self._label_mapview.setObjectName("_label_mapview")
        self.L = QtWidgets.QComboBox(self.centralwidget)
        self.L.setGeometry(QtCore.QRect(10, 190, 91, 22))
        self.L.setFocusPolicy(QtCore.Qt.NoFocus)
        self.L.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.L.setObjectName("L")
        self.L.addItem("")
        self.L.addItem("")
        self.L.addItem("")
        self.L.addItem("")
        self.Search_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_text.setGeometry(QtCore.QRect(430, 570, 301, 20))
        self.Search_text.setMouseTracking(False)
        self.Search_text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Search_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Search_text.setText("")
        self.Search_text.setObjectName("Search_text")
        self._label_search = QtWidgets.QLabel(self.centralwidget)
        self._label_search.setGeometry(QtCore.QRect(430, 550, 131, 16))
        font = QtGui.QFont()
        font.setFamily("SamsungOneUI Medium Condensed")
        font.setPointSize(14)
        self._label_search.setFont(font)
        self._label_search.setStyleSheet("color: rgb(255, 255, 255);")
        self._label_search.setObjectName("_label_search")
        self.Search_button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_button.setGeometry(QtCore.QRect(750, 560, 151, 31))
        self.Search_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Search_button.setStyleSheet("background-color: rgb(13, 13, 13);\n"
"                               font: 63 8pt \\\"Bahnschrift SemiBold\\\";\n"
"                               color:rgb(255, 255, 255);\n"
"                               border-style:outset;\n"
"                               border-width:4px;\n"
"                               border-radius:15px;\n"
"                               border-color:rgb(30, 30, 30)")
        self.Search_button.setObjectName("Search_button")
        self.Search_button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Search_button_cancel.setGeometry(QtCore.QRect(910, 560, 71, 31))
        self.Search_button_cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Search_button_cancel.setStyleSheet("background-color: rgb(13, 13, 13);\n"
"                               font: 63 8pt \\\"Bahnschrift SemiBold\\\";\n"
"                               color:rgb(255, 255, 255);\n"
"                               border-style:outset;\n"
"                               border-width:4px;\n"
"                               border-radius:15px;\n"
"                               border-color:rgb(30, 30, 30)")
        self.Search_button_cancel.setObjectName("Search_button_cancel")
        self.Index_check = QtWidgets.QCheckBox(self.centralwidget)
        self.Index_check.setGeometry(QtCore.QRect(430, 520, 151, 17))
        self.Index_check.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Index_check.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"SamsungOneUILatin 700C\";")
        self.Index_check.setObjectName("Index_check")
        self.Search_result = QtWidgets.QListWidget(self.centralwidget)
        self.Search_result.setGeometry(QtCore.QRect(430, 600, 611, 192))
        self.Search_result.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 18pt \"SamsungOneUI\";")
        self.Search_result.setObjectName("Search_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LL.setText(_translate("MainWindow", "36.193015,51.730846"))
        self._label_cords.setText(_translate("MainWindow", "Координаты"))
        self._label_ms.setText(_translate("MainWindow", "Масштаб"))
        self.Spn.setText(_translate("MainWindow", "0.5,0.5"))
        self._label_mapview.setText(_translate("MainWindow", "Вид карты"))
        self.L.setItemText(0, _translate("MainWindow", "map"))
        self.L.setItemText(1, _translate("MainWindow", "sat"))
        self.L.setItemText(2, _translate("MainWindow", "skl"))
        self.L.setItemText(3, _translate("MainWindow", "trf"))
        self._label_search.setText(_translate("MainWindow", "Поиск"))
        self.Search_button.setText(_translate("MainWindow", "Искать"))
        self.Search_button_cancel.setText(_translate("MainWindow", "Отмена"))
        self.Index_check.setText(_translate("MainWindow", "Отобразить индекс?"))
