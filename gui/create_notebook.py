# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_notebook.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_create_book(object):
    def setupUi(self, create_book):
        create_book.setObjectName("create_book")
        create_book.resize(800, 300)
        create_book.setWindowOpacity(0.9)
        create_book.setStyleSheet("background-color: rgb(26, 26, 26);\n"
"font: \"IosevkaTerm Nerd Font\";")
        self.centralwidget = QtWidgets.QWidget(create_book)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(100, 100, 100);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_close = QtWidgets.QPushButton(self.frame)
        self.bt_close.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Cerrar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_close.setIcon(icon)
        self.bt_close.setIconSize(QtCore.QSize(30, 30))
        self.bt_close.setObjectName("bt_close")
        self.horizontalLayout.addWidget(self.bt_close)
        spacerItem = QtWidgets.QSpacerItem(691, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(800, 0))
        self.frame_2.setStyleSheet("QLabel {\n"
"    Color: rgb(255,255,255); \n"
"}\n"
"QLineEdit{\n"
"    background-color: rgb(204, 204, 204);\n"
"}\n"
"QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(133, 0, 104);\n"
"    border-radius: 20%;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0,0,0)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("IosevkaTerm Nerd Font")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("IosevkaTerm Nerd Font")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_name = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("IosevkaTerm Nerd Font")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.line_name.setFont(font)
        self.line_name.setObjectName("line_name")
        self.horizontalLayout_3.addWidget(self.line_name)
        self.line_teme = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("IosevkaTerm Nerd Font")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.line_teme.setFont(font)
        self.line_teme.setObjectName("line_teme")
        self.horizontalLayout_3.addWidget(self.line_teme)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("IosevkaTerm Nerd Font")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{ \n"
"    background-color: rgb(100,100,100)\n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_path = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("IosevkaTerm Nerd Font")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.line_path.setFont(font)
        self.line_path.setObjectName("line_path")
        self.horizontalLayout_2.addWidget(self.line_path)
        self.bt_search = QtWidgets.QPushButton(self.frame_3)
        self.bt_search.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("IosevkaTerm Nerd Font")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bt_search.setFont(font)
        self.bt_search.setObjectName("bt_search")
        self.horizontalLayout_2.addWidget(self.bt_search)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.bt_create = QtWidgets.QPushButton(self.frame_2)
        self.bt_create.setMinimumSize(QtCore.QSize(300, 40))
        self.bt_create.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("IosevkaTerm Nerd Font")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bt_create.setFont(font)
        self.bt_create.setObjectName("bt_create")
        self.verticalLayout_2.addWidget(self.bt_create, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        create_book.setCentralWidget(self.centralwidget)

        self.retranslateUi(create_book)
        QtCore.QMetaObject.connectSlotsByName(create_book)

    def retranslateUi(self, create_book):
        _translate = QtCore.QCoreApplication.translate
        create_book.setWindowTitle(_translate("create_book", "MainWindow"))
        self.label.setText(_translate("create_book", "Nombre del cuaderno"))
        self.label_3.setText(_translate("create_book", "Tema"))
        self.label_2.setText(_translate("create_book", "Ruta"))
        self.bt_search.setText(_translate("create_book", ""))
        self.bt_create.setText(_translate("create_book", "Crear"))
