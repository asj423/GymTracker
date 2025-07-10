from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel, QWidget, QLineEdit, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
)

class Ui_goalwidgetDisplay(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(500, 400)

        widget.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
                font-family: 'Segoe UI';
                font-size: 14px;
                color: #2c3e50;
            }
            QLabel#label {
                color: #2c3e50;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            QLabel {
                color: #2c3e50;
                font-size: 16px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 6px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QPushButton {
                padding: 8px;
                border: none;
                border-radius: 6px;
                background-color: #007BFF;
                color: white;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QListWidget {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 6px;
                font-size: 14px;
                color: #2c3e50;
            }
        """)

        self.main_layout = QVBoxLayout(widget)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(20)

        self.label = QLabel("Your Goals", widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label)

        self.goalList = QListWidget(widget)
        self.goalList.setObjectName(u"goalList")
        self.main_layout.addWidget(self.goalList)

        self.input_layout = QHBoxLayout()
        self.input_layout.setSpacing(10)

        self.inputGoal = QLineEdit(widget)
        self.inputGoal.setObjectName(u"inputGoal")
        self.input_layout.addWidget(self.inputGoal)

        self.addgoal = QPushButton("+", widget)
        self.addgoal.setObjectName(u"addgoal")
        self.addgoal.setFixedWidth(50)
        self.input_layout.addWidget(self.addgoal)

        self.removegoal = QPushButton("-", widget)
        self.removegoal.setObjectName(u"removegoal")
        self.removegoal.setFixedWidth(50)
        self.input_layout.addWidget(self.removegoal)

        self.main_layout.addLayout(self.input_layout)

    def retranslateUi(self, widget):
        widget.setWindowTitle("Goal Tracker")
        self.label.setText("Your Goals")
        self.addgoal.setText("+")
        self.removegoal.setText("-")