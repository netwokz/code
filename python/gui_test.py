# Building the Window Interface
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from ping_test import ping

servers = ["10.79.217.11"]


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,400,300)
    width = win.frameGeometry().width()
    height = win.frameGeometry().height()
    win.setWindowTitle("Pyqt6 Tutorial")

    button = QtWidgets.QPushButton(win)
    button.setText("Hi! Click Me")
    button.move(50,50)
    button.clicked.connect(click)

    label = QLabel(win)
    label.resize(125,50)
    label.setStyleSheet("border: 1px solid black;")
    label.move(100, 100)
    label.setText(str(ping(servers[0])))
    
    win.show()
    sys.exit(app.exec())
    
def click():
    print("Hy Button is clicked!")

main()