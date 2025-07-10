from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel, QWidget, QComboBox, QVBoxLayout, QHBoxLayout, QSizePolicy, QFrame
)

class Ui_progressDisplay(object):
    def setupUi(self, progressDisplay):
        if not progressDisplay.objectName():
            progressDisplay.setObjectName(u"progressDisplay")
        progressDisplay.resize(900, 900)  # You can manually adjust window size here

        progressDisplay.setStyleSheet("""
            QWidget {
                background-color: #f0f2f5;
                font-family: 'Segoe UI';
                font-size: 14px;
                color: #2c3e50;
            }
            QLabel#label {
                font-size: 32px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 20px;
            }
            QLabel, QComboBox {
                font-size: 16px;
                color: #2c3e50;
            }
            QComboBox {
                padding: 6px;
                border: 1px solid #ccc;
                border-radius: 6px;
                background-color: #ffffff;
            }
            QFrame#progressGraph {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 10px;
            }
        """)

        self.main_layout = QVBoxLayout(progressDisplay)
        self.main_layout.setContentsMargins(10, 10, 10, 10)  # You can manually adjust margins here (left, top, right, bottom)
        self.main_layout.setSpacing(20)
        self.main_layout.setAlignment(Qt.AlignTop)

        self.label = QLabel("Progress Tracker", progressDisplay)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label)

        self.exerciseMenu = QComboBox(progressDisplay)
        self.exerciseMenu.setObjectName(u"exerciseMenu")
        self.exerciseMenu.addItem("Bench Press")
        self.exerciseMenu.addItem("Squats")
        self.exerciseMenu.setFixedHeight(40)
        self.main_layout.addWidget(self.exerciseMenu)

        self.progressGraph = QFrame(progressDisplay)
        self.progressGraph.setObjectName(u"progressGraph")
        self.progressGraph.setMinimumHeight(190)  # You can manually adjust minimum height here
        self.progressGraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addWidget(self.progressGraph)

    def retranslateUi(self, progressDisplay):
        progressDisplay.setWindowTitle("Progress Tracker")
        self.exerciseMenu.setItemText(0, "exercise 1")
        self.exerciseMenu.setItemText(1, "exercise 2")


