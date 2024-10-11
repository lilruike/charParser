# 实现.txt进入显示整个文本的十六进制
# 在查看器中查看到不同的编码格式 常见的编码（如ASCII码， GB2312码，GBK码，Big5，UTF-8，UTF-16）
# word count
# word search
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'mainWindowCaxyVC.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from PySide6 import QtCore, QtWidgets, QtGui
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QRadioButton, QSizePolicy, QStatusBar, QTabWidget,
                               QTableView, QVBoxLayout, QWidget, QFileDialog)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(546, 401)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 121, 321))
        self.groupBox.setStyleSheet(u"border-color: rgb(255, 255, 0);\n"
                                    "background-color: rgb(255, 170, 255);")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 81, 301))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ASCIIButton = QPushButton(self.verticalLayoutWidget)
        self.ASCIIButton.setObjectName(u"ASCIIButton")
        self.ASCIIButton.setCheckable(True)

        self.verticalLayout.addWidget(self.ASCIIButton)

        self.GB2312Button = QPushButton(self.verticalLayoutWidget)
        self.GB2312Button.setObjectName(u"GB2312Button")
        self.GB2312Button.setCheckable(True)

        self.verticalLayout.addWidget(self.GB2312Button)

        self.GBKButton = QPushButton(self.verticalLayoutWidget)
        self.GBKButton.setObjectName(u"GBKButton")
        self.GBKButton.setCheckable(True)

        self.verticalLayout.addWidget(self.GBKButton)

        self.Big5Button = QPushButton(self.verticalLayoutWidget)
        self.Big5Button.setObjectName(u"Big5Button")
        self.Big5Button.setCheckable(True)

        self.verticalLayout.addWidget(self.Big5Button)

        self.UTF8Button = QPushButton(self.verticalLayoutWidget)
        self.UTF8Button.setObjectName(u"UTF8Button")
        self.UTF8Button.setCheckable(True)

        self.verticalLayout.addWidget(self.UTF8Button)

        self.UTF16Button = QPushButton(self.verticalLayoutWidget)
        self.UTF16Button.setObjectName(u"UTF16Button")
        self.UTF16Button.setCheckable(True)

        self.verticalLayout.addWidget(self.UTF16Button)

        self.selectButton = QPushButton(self.centralwidget)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setGeometry(QRect(14, 10, 111, 31))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(150, 9, 371, 61))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.widget = QWidget(self.tab_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, 0, 361, 31))
        self.widget.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 361, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.widget_2 = QWidget(self.tab_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-1, 0, 361, 31))
        self.horizontalLayoutWidget_2 = QWidget(self.widget_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(9, 0, 351, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.radioButton_2 = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.serachButton = QPushButton(self.horizontalLayoutWidget_2)
        self.serachButton.setObjectName(u"serachButton")

        self.horizontalLayout_2.addWidget(self.serachButton)

        self.tabWidget.addTab(self.tab_4, "")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(150, 70, 371, 301))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u683c\u5f0f", None))
        self.ASCIIButton.setText(QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.GB2312Button.setText(QCoreApplication.translate("MainWindow", u"GB2312", None))
        self.GBKButton.setText(QCoreApplication.translate("MainWindow", u"GBK", None))
        self.Big5Button.setText(QCoreApplication.translate("MainWindow", u"Big5", None))
        self.UTF8Button.setText(QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.UTF16Button.setText(QCoreApplication.translate("MainWindow", u"UTF-16", None))
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u7f16\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u8f6c\u6362", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6587\u5b57\u6570\u76ee", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u8282\u6570\u76ee", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QCoreApplication.translate("MainWindow", u"\u6587\u5b57\u8ba1\u6570", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u6587\u5b57", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u5b57\u8282", None))
        self.serachButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4),
                                  QCoreApplication.translate("MainWindow", u"\u6587\u5b57\u67e5\u8be2", None))
    # retranslateUi


class HexModel(QtCore.QAbstractTableModel):
    def __init__(self, data, character_encoding='utf-8', parent=None):
        super(HexModel, self).__init__(parent)
        self._data = data
        self.character_encoding = character_encoding
        # print(data)

    def rowCount(self, parent=None):
        return (len(self._data) + 15) // 16

    def columnCount(self, parent=None):
        return 17  # 16 columns for hex values, 1 for the text representation

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            byte_index = index.row() * 16 + index.column()
            if index.column() < 16:  # 十六进制表示
                if byte_index < len(self._data):  # 确保不超出数据范围
                    return '{:02X}'.format(self._data[byte_index])
                else:
                    return "  "  # 数据不满16字节的部分用空字符串填充
            else:  # 文本表示
                if index.column() == 16:  # 只在最后一列处理文本
                    unit = 16
                    start = index.row() * unit
                    end = min(start + unit, len(self._data))
                    bytes_slice = self._data[start:end]
                    try:
                        # 解码整个字节切片
                        decoded_text = bytes_slice.decode(self.character_encoding, errors='strict')
                        # 用点填充无法显示的字符
                        printable_text = ''.join(c if c.isprintable() else '·' for c in decoded_text)
                        return printable_text
                    except UnicodeDecodeError as e:
                        # 如果在行的中间遇到解码错误，尝试解码直到出错的部分
                        valid_text = bytes_slice[:e.start].decode(self.character_encoding, errors='strict')
                        # 用点填充解码错误后的剩余部分
                        return valid_text + '.' * (unit - len(valid_text))
                    # except LookupError:
                    #     print("编码错误")
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section < 16:
                    return '{:X}'.format(section)
                else:
                    return 'Text'
            else:
                return '{:010X}'.format(section * 16)


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.save_filepath = None
        self.setupUi(self)
        self.open_file_path = None
        self.selectButton.clicked.connect(self.open_file)
        self.nowCoding = 'utf-8'
        self.charButtons = [self.UTF8Button, self.UTF16Button, self.GB2312Button, self.GBKButton, self.ASCIIButton,
                            self.Big5Button]

        for btn in self.charButtons:
            btn.setCheckable(True)
            btn.clicked.connect(self.button_clicked)

    def button_clicked(self):
        clicked_button = self.sender()
        # 还原其他未被点击的按钮
        for button in self.charButtons:
            if button != clicked_button:
                button.setChecked(False)
        self.nowCoding = clicked_button.text()
        self.decode(self.nowCoding)
        # print(self.nowCoding)

    def decode(self, character_encoding):
        file_path = self.open_file_path
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                data = file.read()
                hexModel = HexModel(data, character_encoding)
                self.tableView.setModel(hexModel)
                self.tableView.resizeColumnsToContents()
                self.tableView.setColumnWidth(16, 200)  # You may need to adjust this width
        else:
            print("文件不存在")

    def open_file(self):
        if self.open_file_path is None:
            self.open_file_path, _ = QFileDialog.getOpenFileName(None, '打开文本文件(路径尽量不要有中文)', '', '')
        try:
            # 替换为单反斜杠
            self.open_file_path = str(self.open_file_path).replace("/", "\\").replace(":", ":")
            self.open_file_name = os.path.basename(self.open_file_path)
            if self.open_file_path is not None and self.open_file_path != "":
                self.decode(str(self.nowCoding))
        except:
            print("取消打开文件")

    def save_file(self):
        self.save_file_path, _ = QFileDialog.getSaveFileName(None, '保存文本文件(路径尽量不要有中文)', '', '(*.txt)')
        try:
            # 替换为单反斜杠
            self.save_filepath = str(self.save_file_path).replace("/", "\\").replace(":", ":")
            print(self.save_filepath)
        except:
            print("取消保存文件")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = mainWindow()
    # widget.resize(300, 200)
    widget.show()

    sys.exit(app.exec())

# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.button = QtWidgets.QPushButton("点这里")
#
#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.button)
#
#         self.button.clicked.connect(self.showMessage)
#
#     @QtCore.Slot()
#     def showMessage(self):
#         msgBox = QtWidgets.QMessageBox()
#         msgBox.setText("Hello world")
#         msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
#         ret = msgBox.exec()
