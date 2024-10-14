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
                           QPalette, QPixmap, QRadialGradient, QTransform, QTextCursor, QTextCharFormat)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QRadioButton, QSizePolicy, QStatusBar, QTabWidget,
                               QTableView, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QTextEdit)

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
                               QTableView, QTextEdit, QVBoxLayout, QWidget)

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
                               QTableView, QTextEdit, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(546, 432)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 541, 401))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.selectButton = QPushButton(self.layoutWidget)
        self.selectButton.setObjectName(u"selectButton")

        self.verticalLayout_3.addWidget(self.selectButton)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"border-color: rgb(255, 255, 0);\n"
                                    "background-color: rgb(255, 170, 255);")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 105, 301))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 10, 15, 10)
        self.ASCIIButton = QPushButton(self.verticalLayoutWidget)
        self.ASCIIButton.setObjectName(u"ASCIIButton")
        self.ASCIIButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ASCIIButton.setCheckable(True)

        self.verticalLayout.addWidget(self.ASCIIButton)

        self.GB2312Button = QPushButton(self.verticalLayoutWidget)
        self.GB2312Button.setObjectName(u"GB2312Button")
        self.GB2312Button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.GB2312Button.setCheckable(True)

        self.verticalLayout.addWidget(self.GB2312Button)

        self.GBKButton = QPushButton(self.verticalLayoutWidget)
        self.GBKButton.setObjectName(u"GBKButton")
        self.GBKButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.GBKButton.setCheckable(True)

        self.verticalLayout.addWidget(self.GBKButton)

        self.Big5Button = QPushButton(self.verticalLayoutWidget)
        self.Big5Button.setObjectName(u"Big5Button")
        self.Big5Button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Big5Button.setCheckable(True)

        self.verticalLayout.addWidget(self.Big5Button)

        self.UTF8Button = QPushButton(self.verticalLayoutWidget)
        self.UTF8Button.setObjectName(u"UTF8Button")
        self.UTF8Button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.UTF8Button.setCheckable(True)

        self.verticalLayout.addWidget(self.UTF8Button)

        self.UTF16Button = QPushButton(self.verticalLayoutWidget)
        self.UTF16Button.setObjectName(u"UTF16Button")
        self.UTF16Button.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.UTF16Button.setCheckable(True)

        self.verticalLayout.addWidget(self.UTF16Button)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)

        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.tabWidget = QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
        self.tab.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.widget = QWidget(self.tab_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, 0, 361, 31))
        self.widget.setStyleSheet(u"")
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 361, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setStyleSheet(u"background-color: rgb(0, 255, 255);")
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
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                    "")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.radioButton_2 = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.serachButton = QPushButton(self.horizontalLayoutWidget_2)
        self.serachButton.setObjectName(u"serachButton")
        self.serachButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.serachButton)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.tableView = QTableView(self.layoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
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
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u683c\u5f0f", None))
        self.ASCIIButton.setText(QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.GB2312Button.setText(QCoreApplication.translate("MainWindow", u"GB2312", None))
        self.GBKButton.setText(QCoreApplication.translate("MainWindow", u"GBK", None))
        self.Big5Button.setText(QCoreApplication.translate("MainWindow", u"Big5", None))
        self.UTF8Button.setText(QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.UTF16Button.setText(QCoreApplication.translate("MainWindow", u"UTF-16", None))
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
        self._background_colors = {}  # 用来存储每个单元格的背景颜色
        # print(data)

    def rowCount(self, parent=None):
        return (len(self._data) + 15) // 16

    def columnCount(self, parent=None):
        # return 17  # 16 columns for hex values, 1 for the text representation
        return 16

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            byte_index = index.row() * 16 + index.column()
            if index.column() < 16:  # 十六进制表示
                if byte_index < len(self._data):  # 确保不超出数据范围
                    return '{:02X}'.format(self._data[byte_index])
                else:
                    return "  "  # 数据不满16字节的部分用空字符串填充
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        if role == Qt.BackgroundRole:
            # 返回该单元格的背景颜色（如果有）
            return self._background_colors.get((index.row(), index.column()), QColor(Qt.white))

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False

        if role == Qt.EditRole:
            # 处理数据的编辑逻辑，这里可以扩展为支持修改文本
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True

        if role == Qt.BackgroundRole:
            # 设置该单元格的背景颜色
            self._background_colors[(index.row(), index.column())] = value
            self.dataChanged.emit(index, index, [Qt.BackgroundRole])
            return True

        return False

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
        self.centralwidget.setLayout(self.horizontalLayout_3)
        self.groupBox.setLayout(self.verticalLayout)
        self.open_file_path = None
        self.open_file_name = None
        self.selectButton.clicked.connect(self.open_file)
        self.nowCoding = 'utf-8'
        # self.convertCoding = None
        self.charButtons = [self.UTF8Button, self.UTF16Button, self.GB2312Button, self.GBKButton, self.ASCIIButton,
                            self.Big5Button]

        for btn in self.charButtons:
            btn.setCheckable(True)
            btn.clicked.connect(self.button_clicked)
            btn.clicked.connect(self.statusBarChange)

        self.tabWidget.currentChanged.connect(self.statusBarChange)
        self.serachButton.clicked.connect(self.wordSearch)

    def statusBarChange(self):
        # 获取当前选中的Tab文本
        current_tab_text = self.tabWidget.tabText(self.tabWidget.currentIndex())
        # 获取所有按钮的文本
        # buttons_text = ", ".join([button.text() for button in self.buttons])
        buttons_text = str(self.nowCoding)
        for btn in self.charButtons:
            if btn.isChecked():
                buttons_text = btn.text()
                break
        if buttons_text is None:
            buttons_text = "默认utf-8"
        # 更新状态栏的文本
        self.statusbar.showMessage(
            f"当前模式: {current_tab_text} | 当前编码: {buttons_text} | 文件：{self.open_file_name}")

    def showText(self, data, character_encoding):
        # all_len=len(data)
        try:
            # 解码整个字节切片
            decoded_text = data.decode(character_encoding, errors='strict')
            # 用.填充无法显示的字符
            printable_text = ''.join(c if c.isprintable() else '.' for c in decoded_text)
            # return printable_text
            self.textEdit.setText(printable_text)
        except UnicodeDecodeError as e:
            # 如果在行的中间遇到解码错误，尝试解码直到出错的部分
            valid_text = data.decode(character_encoding, errors='replace')
            # 用点填充解码错误后的剩余部分
            # return valid_text + '.' * (len(data) + len(valid_text))
            self.textEdit.setText(valid_text + '.' * (len(data) - len(valid_text)))

    def button_clicked(self):
        clicked_button = self.sender()
        ind = self.tabWidget.currentIndex()
        # self.buttonCheckedClean()
        if ind == 0:
            self.nowCoding = clicked_button.text()
            self.buttonCheckedClean()
            clicked_button.setChecked(False)
            self.fileDecode(str(self.nowCoding))
        elif ind == 1:
            self.convertButton(str(self.nowCoding))
        elif ind == 2:
            self.buttonCheckedClean()
            self.nowCoding = clicked_button.text()
            self.fileDecode(str(self.nowCoding))
            self.wordCount()
        elif ind == 3:
            self.nowCoding = clicked_button.text()
            self.fileDecode(str(self.nowCoding))
            self.buttonCheckedClean()

    def fileDecode(self, character_encoding):
        file_path = self.open_file_path
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                data = file.read()
                self.showText(data, character_encoding)
                hexModel = HexModel(data, character_encoding)
                self.tableView.setModel(hexModel)
                self.tableView.resizeColumnsToContents()
                self.tableView.setColumnWidth(16, 200)  # You may need to adjust this width
        else:
            print("文件不存在")
            QMessageBox().warning(self, "警告", "文件不存在")

    def open_file(self):
        if self.open_file_path is None:
            self.open_file_path, _ = QFileDialog.getOpenFileName(None, '打开文本文件', '', '')
        try:
            # 替换为单反斜杠
            self.open_file_path = str(self.open_file_path).replace("/", "\\").replace(":", ":")
            self.open_file_name = os.path.basename(self.open_file_path)
            if self.open_file_path is not None and self.open_file_path != "":
                self.fileDecode(str(self.nowCoding))
            self.statusBarChange()
        except:
            print("取消打开文件")
            QMessageBox().warning(self, "警告", "取消打开文件")

    def save_file(self):
        self.save_file_path, _ = QFileDialog.getSaveFileName(None, '保存文本文件', '', '(*.txt)')
        try:
            # 替换为单反斜杠
            self.save_filepath = str(self.save_file_path).replace("/", "\\").replace(":", ":")
        except:
            print("取消保存文件")
            QMessageBox().warning(self, "警告", "取消保存文件")

    def buttonCheckedClean(self):
        for btn in self.charButtons:
            btn.setChecked(False)

    def convertButton(self, formerCoding):
        target_encoding = "tar"
        for btn in self.charButtons:
            if btn.isChecked():
                target_encoding = btn.text()
                if not self.convert_and_save_file(formerCoding, target_encoding):
                    self.nowCoding = formerCoding
                    self.fileDecode(formerCoding)
                    return

    def convert_and_save_file(self, character_encoding, character_decoding):
        # 获取保存路径
        self.save_file()
        # 读取原始文件
        with open(self.open_file_path, 'rb') as file:
            raw_data = file.read()
        # 解码
        try:
            decoded_data = raw_data.decode(character_encoding)
        except UnicodeDecodeError:
            print("原始文件解码失败")
            QMessageBox().warning(self, "警告", f"文本文件{self.open_file_name}以{character_encoding}解码失败",
                                  )
            return False
        # 重新编码
        try:
            encoded_data = decoded_data.encode(character_decoding)
        except:
            print(f"未知的编码格式: {character_decoding}")
            QMessageBox().warning(self, "警告", f"{character_encoding}中有无法转为{character_decoding}的字符")
            return False
        # 保存到新文件
        if self.save_file_path is not None and self.save_file_path != "":
            with open(self.save_file_path, 'wb') as file:
                file.write(encoded_data)
            print(f"文件已保存到 {self.save_file_path}")
            QMessageBox().information(self, "提示", "新编码格式文件已保存")
            # 显示转换后的文件编码
            file_path = self.save_file_path
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    data = file.read()
                    hexModel = HexModel(data, character_decoding)
                    self.tableView.setModel(hexModel)
                    self.tableView.resizeColumnsToContents()
                    self.tableView.setColumnWidth(16, 200)
                    self.showText(data, character_decoding)
                    self.open_file_path = self.save_file_path
                    self.open_file_name = self.open_file_name = os.path.basename(self.open_file_path)
                    self.buttonCheckedClean()
                    self.statusBarChange()
            else:
                QMessageBox().warning(self, "警告", "文件不存在")

    def wordCount(self):
        non_empty_count = 0
        model = self.tableView.model()
        rows = model.rowCount()
        cols = model.columnCount()

        for row in range(rows):
            for col in range(cols):
                index = model.index(row, col)  # 获取模型中指定行列的索引
                data = model.data(index, Qt.DisplayRole)  # 获取显示角色的数据
                if data and data.strip() not in ["", "  "]:
                    non_empty_count += 1
        self.label_4.setText(str(non_empty_count))
        self.label_3.setText(str(len(self.textEdit.toPlainText())))

    def cleanViewColor(self):
        model = self.tableView.model()
        rows = model.rowCount()
        cols = model.columnCount()
        for row in range(rows):
            for col in range(cols):
                index = model.index(row, col)
                model.setData(index, QColor(Qt.white), Qt.BackgroundRole)

    def wordSearch(self):
        # 查询字节
        self.cleanViewColor()
        if self.radioButton.isChecked():
            model = self.tableView.model()
            found = False
            hex_value = self.lineEdit.text()
            rows = model.rowCount()
            cols = model.columnCount()

            for row in range(rows):
                for col in range(cols):
                    index = model.index(row, col)
                    cell_value = model.data(index, Qt.DisplayRole)
                    model.setData(index, QColor(Qt.white), Qt.BackgroundRole)
                    if cell_value == hex_value:
                        model.setData(index, QColor(Qt.green), Qt.BackgroundRole)  # 设置背景为绿色
                        found = True
            if found:
                return
            else:
                for row in range(rows):
                    for col in range(cols):
                        index = model.index(row, col)
                        model.setData(index, QColor(Qt.red), Qt.BackgroundRole)  # 设置背景为红色

        if self.radioButton_2.isChecked():

            input_text = self.lineEdit.text()

            # 创建光标并选择所有文本
            cursor = self.textEdit.textCursor()
            # cursor.select(QTextCursor.Document)  # 选择整个文档
            # cursor.mergeCharFormat(QTextCharFormat())  # 清除原有格式
            #
            # # 重新设置所有文本为黑色
            # self.textEdit.setTextColor(QColor(0, 0, 0))  # 恢复为黑色

            if input_text != "":
                # 创建 QTextCharFormat 用于设置颜色
                format_match = QTextCharFormat()
                format_match.setForeground(QColor(0, 255, 0))  # 设置为绿色
                # 找到匹配的内容并设置颜色
                cursor = self.textEdit.textCursor()
                cursor.setPosition(0)
                found_match = False  # 用于跟踪是否找到匹配

                while True:
                    cursor = self.textEdit.document().find(input_text, cursor)
                    if cursor.isNull():
                        break
                    cursor.mergeCharFormat(format_match)
                    found_match = True  # 找到至少一个匹配

                if not found_match:
                    # 如果没有找到匹配，设置所有文字为红色
                    self.textEdit.selectAll()
                    self.textEdit.setTextColor(QColor(255, 0, 0))  # 设置为红色
                    cursor.mergeCharFormat(format_match)
            else:
                # 如果输入框为空，恢复为黑色
                self.textEdit.selectAll()
                self.textEdit.setTextColor(QColor(0, 0, 0))
                format_match = QTextCharFormat()
                format_match.setForeground(QColor(0, 0, 0))
            cursor.mergeCharFormat(format_match)

            # 设置光标回到文本末尾
            cursor.movePosition(QTextCursor.End)
            self.textEdit.setTextCursor(cursor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = mainWindow()
    # widget.resize(300, 200)
    widget.show()

    sys.exit(app.exec())
