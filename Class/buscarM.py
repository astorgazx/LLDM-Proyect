from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from models import Miembro
import db
import csv

class BuscarWindow():
    def __init__ (self):
        self.buscar = uic.loadUi('Diseños/buscarM.ui')
        self.startGUI()
        self.buscar.show()
        
        #Poner las cabeceras en la tabla de resultados
        self.buscar.resultadotableWidget.setColumnCount(11)
        self.buscar.resultadotableWidget.setHorizontalHeaderLabels(['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Fecha de Nacimiento', 'Sexo', 'Teléfono', 'Correo', 'Dirección', 'Grado de Estudios', 'Ocupación', 'Estado Civil', 'Lugar de Trabajo', 'Domicilio de Trabajo', 'Horario de Trabajo'])
        #Ajustar el tamaño de las columnas al tamaño del contenido
        self.buscar.resultadotableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
    def startGUI(self):
        self.buscar.searchButton.clicked.connect(self.buscarMiembro)
        self.buscar.cancelButton.clicked.connect(self.buscar.close)
        self.buscar.exportButton.clicked.connect(self.exportar)
        
    def buscarMiembro(self):
        # Obtener el campo seleccionado en el combo box
        campo = self.buscar.Optioncombo.currentText()
        # Obtener el valor del campo de texto
        valor = self.buscar.inputTxt.text()
        
        
        
        miembro = None
        
        # Realizar la búsqueda en la base de datos
        if campo == 'Nombre':
            miembro = db.session.query(Miembro).filter(Miembro.nombre == valor).all()
        elif campo == 'Apellido Paterno':
            miembro = db.session.query(Miembro).filter(Miembro.apellidoPaterno == valor).all()
        elif campo == 'Apellido Materno':
            miembro = db.session.query(Miembro).filter(Miembro.apellidoMaterno == valor).all()
        elif campo == 'Ocupación':
            miembro = db.session.query(Miembro).filter(Miembro.ocupacion == valor).all()
        elif campo == 'Estado Civil':
            miembro = db.session.query(Miembro).filter(Miembro.estadoCivil == valor).all()
        elif campo == 'Grado de Estudios':
            miembro = db.session.query(Miembro).filter(Miembro.gradoEstudios == valor).all()
        elif campo == 'Todo':
            miembro = db.session.query(Miembro).all()
            
        # Mostrar los resultados en la tabla
        if miembro:
            print(len(miembro))
            for m in miembro:
                print(m.nombre)
                print(m.apellidoPaterno)
            self.buscar.resultadotableWidget.setRowCount(len(miembro))
            for i, m in enumerate(miembro):
                self.buscar.resultadotableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(m.nombre))
                self.buscar.resultadotableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(m.apellidoPaterno))
                self.buscar.resultadotableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(m.apellidoMaterno))
                self.buscar.resultadotableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(m.fechaNacimiento)))
                self.buscar.resultadotableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(m.sexo))
                self.buscar.resultadotableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(m.telefono))
                self.buscar.resultadotableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(m.correo))
                self.buscar.resultadotableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(m.direccion))
                self.buscar.resultadotableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(m.gradoEstudios))
                self.buscar.resultadotableWidget.setItem(i, 9, QtWidgets.QTableWidgetItem(m.ocupacion))
                self.buscar.resultadotableWidget.setItem(i, 10, QtWidgets.QTableWidgetItem(m.estadoCivil))
                self.buscar.resultadotableWidget.setItem(i, 11, QtWidgets.QTableWidgetItem(m.lugarTrabajo))
                self.buscar.resultadotableWidget.setItem(i, 12, QtWidgets.QTableWidgetItem(m.domicilioTrabajo))
                self.buscar.resultadotableWidget.setItem(i, 13, QtWidgets.QTableWidgetItem(m.horarioTrabajo))
                
        else:
            QMessageBox.warning(self.buscar, 'Error', 'No se encontraron resultados')
            
    def exportar(self):
        # Obtener el nombre del archivo
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self.buscar, 'Exportar a CSV', '', 'CSV Files (*.csv)')

        # Si el usuario no cancela
        if fileName:
            # Crear el archivo
            with open(fileName, 'w') as file:
            # Crear el escritor CSV
                writer = csv.writer(file)

                # Escribir la cabecera
                header = ['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Fecha de Nacimiento', 'Sexo', 'Teléfono', 'Correo', 'Dirección', 'Grado de Estudios', 'Ocupación', 'Estado Civil']
                writer.writerow(header)

                # Escribir los datos
                for i in range(self.buscar.resultadotableWidget.rowCount()):
                    row = []
                    for j in range(self.buscar.resultadotableWidget.columnCount()):
                        row.append(self.buscar.resultadotableWidget.item(i, j).text())
                    writer.writerow(row)

                QMessageBox.information(self.buscar, 'Éxito', 'Datos exportados correctamente')
