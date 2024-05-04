from Class.login import Login
import models
import db


from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication


class Principal():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        
        self.app.exec_()

