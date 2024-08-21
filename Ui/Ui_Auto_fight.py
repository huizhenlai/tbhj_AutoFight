# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Auto_fight.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Auto_fight(object):
    def setupUi(self, Auto_fight):
        if not Auto_fight.objectName():
            Auto_fight.setObjectName(u"Auto_fight")
        Auto_fight.setWindowModality(Qt.NonModal)
        Auto_fight.resize(557, 409)
        self.verticalLayout_6 = QVBoxLayout(Auto_fight)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_1 = QPushButton(Auto_fight)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.verticalLayout.addWidget(self.pushButton_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Auto_fight)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_handle1 = QLineEdit(Auto_fight)
        self.lineEdit_handle1.setObjectName(u"lineEdit_handle1")

        self.horizontalLayout.addWidget(self.lineEdit_handle1)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(Auto_fight)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.lineEdit_title1 = QLineEdit(Auto_fight)
        self.lineEdit_title1.setObjectName(u"lineEdit_title1")

        self.horizontalLayout_4.addWidget(self.lineEdit_title1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(Auto_fight)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Auto_fight)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_handle2 = QLineEdit(Auto_fight)
        self.lineEdit_handle2.setObjectName(u"lineEdit_handle2")

        self.horizontalLayout_2.addWidget(self.lineEdit_handle2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(Auto_fight)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.lineEdit_title2 = QLineEdit(Auto_fight)
        self.lineEdit_title2.setObjectName(u"lineEdit_title2")

        self.horizontalLayout_5.addWidget(self.lineEdit_title2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.label_4 = QLabel(Auto_fight)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.plainTextEdit = QPlainTextEdit(Auto_fight)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.plainTextEdit)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_1 = QLabel(Auto_fight)
        self.label_1.setObjectName(u"label_1")
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_1)

        self.label_9 = QLabel(Auto_fight)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.label_10 = QLabel(Auto_fight)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_A = QLineEdit(Auto_fight)
        self.lineEdit_A.setObjectName(u"lineEdit_A")
        sizePolicy.setHeightForWidth(self.lineEdit_A.sizePolicy().hasHeightForWidth())
        self.lineEdit_A.setSizePolicy(sizePolicy)
        self.lineEdit_A.setTabletTracking(False)
        self.lineEdit_A.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_A)

        self.lineEdit_time = QLineEdit(Auto_fight)
        self.lineEdit_time.setObjectName(u"lineEdit_time")
        sizePolicy.setHeightForWidth(self.lineEdit_time.sizePolicy().hasHeightForWidth())
        self.lineEdit_time.setSizePolicy(sizePolicy)
        self.lineEdit_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_time)

        self.lineEdit_Tab = QLineEdit(Auto_fight)
        self.lineEdit_Tab.setObjectName(u"lineEdit_Tab")
        sizePolicy.setHeightForWidth(self.lineEdit_Tab.sizePolicy().hasHeightForWidth())
        self.lineEdit_Tab.setSizePolicy(sizePolicy)
        self.lineEdit_Tab.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_Tab)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_start_1 = QPushButton(Auto_fight)
        self.pushButton_start_1.setObjectName(u"pushButton_start_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_start_1.sizePolicy().hasHeightForWidth())
        self.pushButton_start_1.setSizePolicy(sizePolicy1)
        self.pushButton_start_1.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_start_1)

        self.pushButton_stop_1 = QPushButton(Auto_fight)
        self.pushButton_stop_1.setObjectName(u"pushButton_stop_1")
        sizePolicy1.setHeightForWidth(self.pushButton_stop_1.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_1.setSizePolicy(sizePolicy1)
        self.pushButton_stop_1.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_stop_1)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_start_2 = QPushButton(Auto_fight)
        self.pushButton_start_2.setObjectName(u"pushButton_start_2")
        sizePolicy1.setHeightForWidth(self.pushButton_start_2.sizePolicy().hasHeightForWidth())
        self.pushButton_start_2.setSizePolicy(sizePolicy1)
        self.pushButton_start_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_start_2)

        self.pushButton_stop_2 = QPushButton(Auto_fight)
        self.pushButton_stop_2.setObjectName(u"pushButton_stop_2")
        sizePolicy1.setHeightForWidth(self.pushButton_stop_2.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_2.setSizePolicy(sizePolicy1)
        self.pushButton_stop_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_stop_2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.label_3 = QLabel(Auto_fight)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)


        self.retranslateUi(Auto_fight)

        QMetaObject.connectSlotsByName(Auto_fight)
    # setupUi

    def retranslateUi(self, Auto_fight):
        Auto_fight.setWindowTitle(QCoreApplication.translate("Auto_fight", u"Auto_fight", None))
        self.pushButton_1.setText(QCoreApplication.translate("Auto_fight", u"\u7a97\u53e31", None))
        self.label.setText(QCoreApplication.translate("Auto_fight", u"\u53e5\u67c4", None))
        self.label_7.setText(QCoreApplication.translate("Auto_fight", u"\u6807\u7b7e", None))
        self.pushButton_2.setText(QCoreApplication.translate("Auto_fight", u"\u7a97\u53e32", None))
        self.label_2.setText(QCoreApplication.translate("Auto_fight", u"\u53e5\u67c4", None))
        self.label_8.setText(QCoreApplication.translate("Auto_fight", u"\u6807\u7b7e", None))
        self.label_4.setText("")
        self.label_1.setText(QCoreApplication.translate("Auto_fight", u"\u653b\u51fb", None))
        self.label_9.setText(QCoreApplication.translate("Auto_fight", u"\u95f4\u9694(ms)", None))
        self.label_10.setText(QCoreApplication.translate("Auto_fight", u"\u5207\u602a", None))
        self.lineEdit_A.setText(QCoreApplication.translate("Auto_fight", u"a", None))
        self.lineEdit_time.setText(QCoreApplication.translate("Auto_fight", u"100", None))
        self.lineEdit_Tab.setText(QCoreApplication.translate("Auto_fight", u"w", None))
        self.pushButton_start_1.setText(QCoreApplication.translate("Auto_fight", u"\u5f00\u59cb1", None))
        self.pushButton_stop_1.setText(QCoreApplication.translate("Auto_fight", u"\u505c\u6b621", None))
        self.pushButton_start_2.setText(QCoreApplication.translate("Auto_fight", u"\u5f00\u59cb2", None))
        self.pushButton_stop_2.setText(QCoreApplication.translate("Auto_fight", u"\u505c\u6b622", None))
        self.label_3.setText(QCoreApplication.translate("Auto_fight", u"\u8bf4\u660e\uff1a\u6309\u4e0b\u5bf9\u5e94\u7a97\u53e3\u6309\u94ae\u4e4b\u540e\uff0c\u9f20\u6807\u9009\u4e2d\u5bf9\u5e94\u6e38\u620f\u7a97\u53e3\u4f4d\u7f6e\uff0c2\u79d2\u4e4b\u540e\u786e\u5b9a\u53e5\u67c4\uff0c\u6700\u591a\u652f\u6301\u53cc\u5f00\u3002", None))
    # retranslateUi

