from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow  # Import converted UI
from progress import ProgressDisplay
from goalwidget import goalwidgetDisplay
from profilewidget import profilewidgetDisplay
from logworkout import logworkoutDisplay
from database_interface import Database

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize UI

        self.database = Database()
        QApplication.instance().aboutToQuit.connect(self.close_database)

        self.progressDisplay = ProgressDisplay(self.database)
        self.display.addWidget(self.progressDisplay)

        self.goalDisplay = goalwidgetDisplay(self.database)
        self.display.addWidget(self.goalDisplay)

        self.profileDisplay = profilewidgetDisplay(self.database)
        self.display.addWidget(self.profileDisplay)

        self.logworkoutDisplay = logworkoutDisplay(self.database)
        self.display.addWidget(self.logworkoutDisplay)

        self.progressButton.clicked.connect(self.progressButtonClicked)
        self.goalButton.clicked.connect(self.goalButtonClicked)
        self.logButton.clicked.connect(self.logButtonClicked)
        self.profileButton.clicked.connect(self.profileButtonClicked)
        self.profileButtonClicked()

    def close_database(self):
        # This is called when application is closing
        if self.database:
            self.database.close()
            print("Closed database!") # testing
        else:
            print("No database connection to close.")

    def progressButtonClicked(self):
        self.display.setCurrentWidget(self.progressDisplay)

    def goalButtonClicked(self):
        self.display.setCurrentWidget(self.goalDisplay)
        
        

    def logButtonClicked(self):
        self.display.setCurrentWidget(self.logworkoutDisplay)

    def profileButtonClicked(self):
        self.display.setCurrentWidget(self.profileDisplay)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()