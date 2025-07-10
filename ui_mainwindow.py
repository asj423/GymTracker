from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QStackedWidget, QStatusBar,
    QMenuBar
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("""
            #centralwidget {
                background-color: #f0f0f0;
            }
        """)

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.headerLabel = QLabel(self.centralwidget)
        self.headerLabel.setObjectName("headerLabel")
        self.headerLabel.setText("🏋️‍♂️ TrackMate Gym")
        self.headerLabel.setAlignment(Qt.AlignCenter)
        self.headerLabel.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #333;
                margin: 10px 0;
            }
        """)
        self.verticalLayout.addWidget(self.headerLabel)

        self.display = QStackedWidget(self.centralwidget)
        self.display.setObjectName("display")
        self.display.setMinimumSize(QSize(0, 350))
        self.display.setStyleSheet("""
            QStackedWidget {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #ccc;
            }
        """)
        self.home = QWidget()
        self.home.setObjectName("home")
        self.display.addWidget(self.home)
        self.verticalLayout.addWidget(self.display)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.buttonLayout.setSpacing(15)
        self.buttonLayout.setContentsMargins(20, 10, 20, 20)

        font = QFont()
        font.setBold(True)

        self.progressButton = QPushButton(self.centralwidget)
        self.progressButton.setObjectName("progressButton")
        self.progressButton.setText("Progress")
        self.progressButton.setFont(font)
        self.progressButton.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.buttonLayout.addWidget(self.progressButton)

        self.goalButton = QPushButton(self.centralwidget)
        self.goalButton.setObjectName("goalButton")
        self.goalButton.setText("Goals")
        self.goalButton.setFont(font)
        self.goalButton.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #138496;
            }
        """)
        self.buttonLayout.addWidget(self.goalButton)

        self.logButton = QPushButton(self.centralwidget)
        self.logButton.setObjectName("logButton")
        self.logButton.setText("LogWorkout")
        self.logButton.setFont(font)
        self.logButton.setStyleSheet("""
            QPushButton {
                background-color: #ffc107;
                color: black;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #e0a800;
            }
        """)
        self.buttonLayout.addWidget(self.logButton)

        self.profileButton = QPushButton(self.centralwidget)
        self.profileButton.setObjectName("profileButton")
        self.profileButton.setText("Profile")
        self.profileButton.setFont(font)
        self.profileButton.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #bd2130;
            }
        """)
        self.buttonLayout.addWidget(self.profileButton)

        self.verticalLayout.addLayout(self.buttonLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.display.setCurrentIndex(0)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("TrackMate Gym")
