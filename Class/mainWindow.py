from PyQt5 import QtWidgets, uic

from Class.editM import EditMiembroWindow
from Class.registro import RegistroWindow

from Class.buscarM import BuscarWindow

from models import Miembro, Matrimonio

import db


class MainWindow():
    def __init__(self):
        self.mainWindow = uic.loadUi('Diseños/mainWindow.ui')
        self.startGUI()
        self.mainWindow.show()
        
    def startGUI(self):
        self.mainWindow.actionRegistrar_Miembro.triggered.connect(self.registrarMiembro)
        self.mainWindow.actionBuscar_Miembro.triggered.connect(self.buscarMiembro)
        self.mainWindow.numeroMiembros.setText(str(self.miembrosTotales()))
        self.mainWindow.numeroMatrimonios.setText(str(self.matrimoniosTotales()))
        self.mainWindow.actionEditar_Miembro.triggered.connect(self.editarMiembro)
        
    def editarMiembro(self):
        print('Editar miembro')
        self.editar = EditMiembroWindow()
        
    def registrarMiembro(self):
        self.registro = RegistroWindow()
        print('Registrar miembro')
        
    def buscarMiembro(self):
        self.buscar = BuscarWindow()
        
    def miembrosTotales(self):
        #Obtener la cantidad de miembros en la base de datos
        miembros = db.session.query(Miembro).all()
        return len(miembros)
    
    def matrimoniosTotales(self):
        #Obtener la cantidad de matrimonios en la base de datos
        matrimonios = db.session.query(Matrimonio).all()
        return len(matrimonios) 
    