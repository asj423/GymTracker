# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logworkout.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_WorkoutLogPage(object):
    def setupUi(self, WorkoutLogPage):
        if not WorkoutLogPage.objectName():
            WorkoutLogPage.setObjectName(u"WorkoutLogPage")
        WorkoutLogPage.resize(659, 539)
        self.verticalLayout = QVBoxLayout(WorkoutLogPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(WorkoutLogPage)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"font-size: 18px; font-weight: bold;")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.dateEdit = QDateEdit(WorkoutLogPage)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.dateEdit)

        self.lineEdit_duration = QLineEdit(WorkoutLogPage)
        self.lineEdit_duration.setObjectName(u"lineEdit_duration")

        self.verticalLayout.addWidget(self.lineEdit_duration)

        self.groupBox_exercises = QGroupBox(WorkoutLogPage)
        self.groupBox_exercises.setObjectName(u"groupBox_exercises")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_exercises)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_exercise = QLineEdit(self.groupBox_exercises)
        self.lineEdit_exercise.setObjectName(u"lineEdit_exercise")

        self.horizontalLayout.addWidget(self.lineEdit_exercise)

        self.lineEdit_sets = QLineEdit(self.groupBox_exercises)
        self.lineEdit_sets.setObjectName(u"lineEdit_sets")

        self.horizontalLayout.addWidget(self.lineEdit_sets)

        self.lineEdit_reps = QLineEdit(self.groupBox_exercises)
        self.lineEdit_reps.setObjectName(u"lineEdit_reps")

        self.horizontalLayout.addWidget(self.lineEdit_reps)

        self.lineEdit_weight = QLineEdit(self.groupBox_exercises)
        self.lineEdit_weight.setObjectName(u"lineEdit_weight")

        self.horizontalLayout.addWidget(self.lineEdit_weight)

        self.pushButton_add = QPushButton(self.groupBox_exercises)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setMouseTracking(False)

        self.horizontalLayout.addWidget(self.pushButton_add)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableWidget_exercises = QTableWidget(self.groupBox_exercises)
        if (self.tableWidget_exercises.columnCount() < 4):
            self.tableWidget_exercises.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_exercises.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_exercises.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_exercises.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_exercises.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_exercises.setObjectName(u"tableWidget_exercises")

        self.verticalLayout_2.addWidget(self.tableWidget_exercises)


        self.verticalLayout.addWidget(self.groupBox_exercises)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_save = QPushButton(WorkoutLogPage)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout_2.addWidget(self.pushButton_save)

        self.pushButton_cancel = QPushButton(WorkoutLogPage)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(WorkoutLogPage)

        QMetaObject.connectSlotsByName(WorkoutLogPage)
    # setupUi

    def retranslateUi(self, WorkoutLogPage):
        WorkoutLogPage.setWindowTitle(QCoreApplication.translate("WorkoutLogPage", u"Workout Logger", None))
        self.label_title.setText(QCoreApplication.translate("WorkoutLogPage", u"TRACKMATE Gym - Log workouts", None))
        self.lineEdit_duration.setPlaceholderText(QCoreApplication.translate("WorkoutLogPage", u"Workout Duration (minutes)", None))
        self.groupBox_exercises.setTitle(QCoreApplication.translate("WorkoutLogPage", u"Exercises", None))
        self.lineEdit_exercise.setPlaceholderText(QCoreApplication.translate("WorkoutLogPage", u"Exercise Name", None))
        self.lineEdit_sets.setPlaceholderText(QCoreApplication.translate("WorkoutLogPage", u"Sets", None))
        self.lineEdit_reps.setPlaceholderText(QCoreApplication.translate("WorkoutLogPage", u"Reps", None))
        self.lineEdit_weight.setPlaceholderText(QCoreApplication.translate("WorkoutLogPage", u"Weight (kg/lbs)", None))
        self.pushButton_add.setText(QCoreApplication.translate("WorkoutLogPage", u"Add", None))
        ___qtablewidgetitem = self.tableWidget_exercises.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WorkoutLogPage", u"Exercise", None));
        ___qtablewidgetitem1 = self.tableWidget_exercises.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WorkoutLogPage", u"Sets", None));
        ___qtablewidgetitem2 = self.tableWidget_exercises.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WorkoutLogPage", u"Reps", None));
        ___qtablewidgetitem3 = self.tableWidget_exercises.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WorkoutLogPage", u"Weight", None));
        self.pushButton_save.setText(QCoreApplication.translate("WorkoutLogPage", u"Save Workout", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("WorkoutLogPage", u"Cancel", None))
    # retranslateUi

