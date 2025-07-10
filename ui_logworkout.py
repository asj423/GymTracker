from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel, QWidget, QLineEdit, QDateEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QTableWidget, QTableWidgetItem, QGroupBox, QFormLayout
)

class Ui_WorkoutLogPage(object):
    def setupUi(self, WorkoutLogPage):
        if not WorkoutLogPage.objectName():
            WorkoutLogPage.setObjectName(u"WorkoutLogPage")
        WorkoutLogPage.resize(850, 900)  # You can manually adjust window size here

        WorkoutLogPage.setStyleSheet("""
            QWidget {
                background-color: #f0f2f5;
                font-family: 'Segoe UI';
                font-size: 14px;
                color: #2c3e50;
            }
            QLabel#label_title {
                font-size: 32px;
                font-weight: bold;
                margin-bottom: 20px;
                color: #2c3e50;
            }
            QLabel, QLineEdit, QDateEdit, QPushButton {
                font-size: 16px;
                color: #2c3e50;
            }
            QLineEdit, QDateEdit {
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: #ffffff;
            }
            QPushButton {
                padding: 10px 20px;
                border-radius: 6px;
                background-color: #3498db;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QGroupBox {
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 20px;
                background-color: #ffffff;
            }
            QTableWidget {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 14px;
                color: #2c3e50;
                gridline-color: #d0d0d0;
            }
        """)

        self.main_layout = QVBoxLayout(WorkoutLogPage)
        self.main_layout.setContentsMargins(20, 20, 20, 20)  # You can manually adjust margins here
        self.main_layout.setSpacing(20)
        self.main_layout.setAlignment(Qt.AlignTop)

        self.label_title = QLabel("TRACKMATE Gym - Log workouts", WorkoutLogPage)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label_title)

        self.dateEdit = QDateEdit(WorkoutLogPage)
        self.dateEdit.setObjectName(u"dateEdit")
        self.main_layout.addWidget(self.dateEdit)

        self.lineEdit_duration = QLineEdit(WorkoutLogPage)
        self.lineEdit_duration.setObjectName(u"lineEdit_duration")
        self.lineEdit_duration.setPlaceholderText("Workout Duration (minutes)")
        self.main_layout.addWidget(self.lineEdit_duration)

        self.groupBox_exercises = QGroupBox("Exercises", WorkoutLogPage)
        self.groupBox_exercises.setObjectName(u"groupBox_exercises")
        self.exercise_layout = QVBoxLayout(self.groupBox_exercises)

        self.input_row = QHBoxLayout()

        self.lineEdit_exercise = QLineEdit(self.groupBox_exercises)
        self.lineEdit_exercise.setObjectName(u"lineEdit_exercise")
        self.lineEdit_exercise.setPlaceholderText("Exercise Name")
        self.input_row.addWidget(self.lineEdit_exercise)

        self.lineEdit_sets = QLineEdit(self.groupBox_exercises)
        self.lineEdit_sets.setObjectName(u"lineEdit_sets")
        self.lineEdit_sets.setPlaceholderText("Sets")
        self.input_row.addWidget(self.lineEdit_sets)

        self.lineEdit_reps = QLineEdit(self.groupBox_exercises)
        self.lineEdit_reps.setObjectName(u"lineEdit_reps")
        self.lineEdit_reps.setPlaceholderText("Reps")
        self.input_row.addWidget(self.lineEdit_reps)

        self.lineEdit_weight = QLineEdit(self.groupBox_exercises)
        self.lineEdit_weight.setObjectName(u"lineEdit_weight")
        self.lineEdit_weight.setPlaceholderText("Weight (kg/lbs)")
        self.input_row.addWidget(self.lineEdit_weight)

        self.pushButton_add = QPushButton("Add", self.groupBox_exercises)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.input_row.addWidget(self.pushButton_add)

        self.exercise_layout.addLayout(self.input_row)

        self.tableWidget_exercises = QTableWidget(self.groupBox_exercises)
        self.tableWidget_exercises.setObjectName(u"tableWidget_exercises")
        self.tableWidget_exercises.setColumnCount(4)
        self.tableWidget_exercises.setHorizontalHeaderLabels(["Exercise", "Sets", "Reps", "Weight"])
        self.exercise_layout.addWidget(self.tableWidget_exercises)

        self.main_layout.addWidget(self.groupBox_exercises)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setSpacing(20)

        self.pushButton_save = QPushButton("Save Workout", WorkoutLogPage)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.bottom_layout.addWidget(self.pushButton_save)

        self.pushButton_cancel = QPushButton("Cancel", WorkoutLogPage)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.bottom_layout.addWidget(self.pushButton_cancel)

        self.main_layout.addLayout(self.bottom_layout)

    def retranslateUi(self, WorkoutLogPage):
        WorkoutLogPage.setWindowTitle("Workout Logger")

