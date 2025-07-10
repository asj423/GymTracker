from PySide6.QtWidgets import QWidget
from ui_profilewidget import Ui_profilewidgetDisplay
import sqlite3

class profilewidgetDisplay(Ui_profilewidgetDisplay, QWidget):

    def __init__(self, database, user_id=1):  # Default to user_id=1, can be changed
        super().__init__()
        self.db = database
        self.setupUi(self)
        self.user_id = user_id
        self.edit_mode = False
        self.load_user_data()
        self.editButton.clicked.connect(self.toggle_edit_mode)

    def load_user_data(self):
        self.userweight = self.db.getBodyweight()
        self.username = self.db.getName()
        self.usergender = self.db.getGender()
        self.userage = self.db.getAge()

        self.name.setText(str(self.username if self.username else ""))
        self.age.setText(str(self.userage if self.userage else ""))
        self.weight.setText(str(self.userweight if self.userweight else ""))
        self.gender.setText(str(self.usergender if self.usergender else ""))

    def toggle_edit_mode(self):
        if not self.edit_mode:
            self.name.setReadOnly(False)
            self.age.setReadOnly(False)
            self.weight.setReadOnly(False)
            self.gender.setReadOnly(False)
            self.editButton.setText("Save")
        else:
            self.name.setReadOnly(True)
            self.age.setReadOnly(True)
            self.weight.setReadOnly(True)
            self.gender.setReadOnly(True)
            self.editButton.setText("Edit")

            self.db.setName(self.name.text())
            self.db.setAge(int(self.age.text()))
            self.db.logBodyweight(float(self.weight.text()))
            self.db.setGender(self.gender.text())

        self.edit_mode = not self.edit_mode
