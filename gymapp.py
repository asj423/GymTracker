# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gymapp.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressButton = QPushButton(self.centralwidget)

        self.progressButton.setObjectName(u"progressButton")
        self.progressButton.setGeometry(QRect(40, 400, 75, 23))
        self.GoalButton = QPushButton(self.centralwidget)

        self.GoalButton.setObjectName(u"GoalButton")
        self.GoalButton.setGeometry(QRect(190, 400, 75, 23))
        self.logButton = QPushButton(self.centralwidget)

        self.logButton.setObjectName(u"logButton")
        self.logButton.setGeometry(QRect(340, 400, 75, 23))
        self.profileButton = QPushButton(self.centralwidget)

        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setGeometry(QRect(540, 400, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.progressButton.setText(QCoreApplication.translate("MainWindow", u"progress", None))
        self.GoalButton.setText(QCoreApplication.translate("MainWindow", u"Goals", None))
        self.logButton.setText(QCoreApplication.translate("MainWindow", u"LogWorkout", None))
        self.profileButton.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressButton.clicked.connect(self.progressButtonClicked)
        self.GoalButton.clicked.connect(self.GoalButtonClicked)
        self.logButton.clicked.connect(self.logButtonClicked)
        self.profileButton.clicked.connect(self.profileButtonClicked)

    def progressButtonClicked(self):
        print("prgress")

    def GoalButtonClicked(self):
        print("goal")

    def logButtonClicked(self):
        print("log")

    def profileButtonClicked(self):
        print("profile")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())