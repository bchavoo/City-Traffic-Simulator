from Controller import Controller
from tkinter import Tk
from PyQt5 import QtCore, QtWidgets

def test_start_button(qtbot):
    root = Tk()
    command = Controller(master=root)
    qtbot.addWidget(command)
    qtbot.mouseClick(command.start_button, QtCore.Qt.LeftButton)