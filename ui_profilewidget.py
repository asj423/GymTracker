from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout, QSizePolicy, QFrame
)

class Ui_profilewidgetDisplay(object):
    def setupUi(self, profilewidgetDisplay):
        if not profilewidgetDisplay.objectName():
            profilewidgetDisplay.setObjectName(u"profilewidgetDisplay")
        profilewidgetDisplay.resize(750, 600)

        profilewidgetDisplay.setStyleSheet("""
            QWidget {
                background-color: #f0f2f5;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel#label {
                font-size: 32px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 20px;
            }
            QFrame#formFrame {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 30px;
                border: 1px solid #d0d0d0;
            }
            QLabel {
                font-size: 16px;
                color: #2c3e50;
            }
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 16px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QLineEdit[readOnly="true"] {
                background-color: #f9f9f9;
                color: #2c3e50;
            }
            QPushButton#editButton {
                border-radius: 10px;
                padding: 12px 30px;
                background-color: #3498db;
                color: white;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton#editButton:hover {
                background-color: #2980b9;
            }
            QPushButton#editButton:pressed {
                background-color: #1c6ea4;
            }
        """)

        self.main_layout = QVBoxLayout(profilewidgetDisplay)
        self.main_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.main_layout.setContentsMargins(40, 40, 40, 40)
        self.main_layout.setSpacing(20)

        self.label = QLabel("Profile", profilewidgetDisplay)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.label)

        self.formFrame = QFrame(profilewidgetDisplay)
        self.formFrame.setObjectName(u"formFrame")
        self.form_layout = QFormLayout(self.formFrame)
        self.form_layout.setSpacing(20)

        # Adjustable box size variables
        box_width = 300
        box_height = 32.5

        # --- Name field ---
        self.name = QLineEdit(self.formFrame)
        self.name.setObjectName(u"name")
        self.name.setReadOnly(True)
        self.name.setFixedSize(box_width, box_height)

        name_label = QLabel("Name:")
        name_label.setMinimumHeight(30)  # <== adjust this if needed
        name_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.form_layout.addRow(name_label, self.name)

        # --- Age field ---
        self.age = QLineEdit(self.formFrame)
        self.age.setObjectName(u"age")
        self.age.setReadOnly(True)
        self.age.setFixedSize(box_width, box_height)

        age_label = QLabel("Age:")
        age_label.setMinimumHeight(30)
        age_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.form_layout.addRow(age_label, self.age)

        # --- Weight field ---
        self.weight = QLineEdit(self.formFrame)
        self.weight.setObjectName(u"weight")
        self.weight.setReadOnly(True)
        self.weight.setFixedSize(box_width, box_height)

        weight_label = QLabel("Weight:")
        weight_label.setMinimumHeight(30)
        weight_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.form_layout.addRow(weight_label, self.weight)

        # --- Gender field ---
        self.gender = QLineEdit(self.formFrame)
        self.gender.setObjectName(u"gender")
        self.gender.setReadOnly(True)
        self.gender.setFixedSize(box_width, box_height)

        gender_label = QLabel("Gender:")
        gender_label.setMinimumHeight(30)
        gender_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.form_layout.addRow(gender_label, self.gender)

        self.main_layout.addWidget(self.formFrame)

        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignCenter)

        self.editButton = QPushButton("Edit", profilewidgetDisplay)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setFixedWidth(200)

        self.button_layout.addWidget(self.editButton)
        self.main_layout.addLayout(self.button_layout)

    def retranslateUi(self, profilewidgetDisplay):
        profilewidgetDisplay.setWindowTitle("Profile")
        self.label.setText("Profile")




