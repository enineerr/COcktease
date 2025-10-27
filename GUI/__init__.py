from PySide6.QtWidgets import QApplication
from GUI.mainWindow import mainWindow
from sys import exit


class GUI:
    def __init__(self):
        app = QApplication()
        main = mainWindow()
        main.show()
        
        # Exit app with exit code of qt widget
        exit(app.exec())