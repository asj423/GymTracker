from PySide6.QtWidgets import QWidget, QMessageBox
from ui_goalwidget import Ui_goalwidgetDisplay
from database_interface import Database


class goalwidgetDisplay(Ui_goalwidgetDisplay, QWidget):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)

        self.db = database
        stufftoadd = self.db.getGoals()

        self.addgoal.clicked.connect(self.add_goal)
        self.removegoal.clicked.connect(self.remove_goal)
        self.inputGoal.setPlaceholderText("Enter your goal")
        self.inputGoal.setVisible(False)
        self.inputGoal.returnPressed.connect(self.add_goal)

        for i in range(len(stufftoadd)):
            self.goalList.addItem(stufftoadd[i])

    def add_goal(self):
        if self.inputGoal.isVisible():
            text = self.inputGoal.text().strip()
            if text:  # only add non-empty text
                self.goalList.addItem(text)
                self.db.addGoal(text)
                self.inputGoal.clear()  # clear after adding
                self.inputGoal.setVisible(False)
        else:
            self.inputGoal.setVisible(True)
            self.inputGoal.setFocus()  # set focus when showing input
        
        
        

    
    def remove_goal(self):
        selected_items = self.goalList.selectedItems()  # Get selected items
        for item in selected_items:
            self.goalList.takeItem(self.goalList.row(item))  # Remove the selected item
            self.db.removeGoal(item.text())
            QMessageBox.information(self, "Goal Removed", "Congratulations on completing your goal!")