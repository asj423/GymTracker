# version of progress.py that didnt work with rest of the code

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi("progress_tracker.ui", self)

        # Setup matplotlib graph
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Add the canvas to the graphContainer
        layout = QVBoxLayout(self.graphContainer)
        layout.addWidget(self.canvas)

        # Example data
        self.dates = ["01/01/2025", "2023-02-01", "2023-03-01", "2023-04-01"]
        self.one_rm = [100, 110, 115, 120]  # 1RM data (kg)
        self.body_weight = [75, 76, 77, 76.5]  # Body weight data (kg)

        # Connect dropdown to update function
        self.graphSelector.currentTextChanged.connect(self.update_graph)

        # Initial graph draw
        self.update_graph()

        # Increase dropdown size
        self.graphSelector.setMinimumSize(200, 40)  # Width, Height

        self.graphSelector.raise_()

    def update_graph(self):
        """Update the graph based on dropdown selection"""
        selected_graph = self.graphSelector.currentText()
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        if selected_graph == "1RM Progress":
            ax.plot(self.dates, self.one_rm, 'o-', color='blue', label='1RM (kg)')
            ax.set_title("1RM Progress Over Time")
            ax.set_ylabel("Weight (kg)")
        else:
            ax.plot(self.dates, self.body_weight, 'o-', color='green', label='Body Weight (kg)')
            ax.set_title("Body Weight Over Time")
            ax.set_ylabel("Weight (kg)")

        # Shared graph settings
        ax.set_xlabel("Date")
        ax.grid(True)
        ax.legend()

        # Rotate date labels
        for label in ax.get_xticklabels():
            label.set_rotation(45)
            label.set_ha('right')

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())