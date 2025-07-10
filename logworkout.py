from PySide6.QtWidgets import QWidget, QTableWidgetItem

from ui_workoutLogPage import Ui_WorkoutLogPage

class logworkoutDisplay(Ui_WorkoutLogPage, QWidget):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.db = database
        self.pushButton_add.clicked.connect(self.add_exercise_to_db)
        self.pushButton_save.clicked.connect(self.save_workout_to_db)

    def add_exercise_to_db(self):
        reps = self.lineEdit_reps.text()
        sets = self.lineEdit_sets.text()
        exercise_name = self.lineEdit_exercise.text()
        weight = self.lineEdit_weight.text()

        if self.db.logExercise(exercise_name, sets, reps, weight):
            self.add_row(exercise_name, sets, reps, weight)

            self.lineEdit_reps.clear()
            self.lineEdit_sets.clear()
            self.lineEdit_exercise.clear()
            self.lineEdit_weight.clear()

    def save_workout_to_db(self):
        duration = self.lineEdit_duration.text()
        try:
            duration = float(duration)
            # lazy
        except:
            return
        self.db.createNewSession(duration)
        self.lineEdit_duration.clear()
        self.tableWidget_exercises.setRowCount(0)
        self.tableWidget_exercises.clearContents()



    def add_row(self, exercise_name, sets, reps, weight):
        row_position = self.tableWidget_exercises.rowCount()
        self.tableWidget_exercises.insertRow(row_position)
        self.tableWidget_exercises.setItem(row_position, 0, QTableWidgetItem(exercise_name))
        self.tableWidget_exercises.setItem(row_position, 1, QTableWidgetItem(sets))
        self.tableWidget_exercises.setItem(row_position, 2, QTableWidgetItem(reps))
        self.tableWidget_exercises.setItem(row_position, 3, QTableWidgetItem(weight))