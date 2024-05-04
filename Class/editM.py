import datetime
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from models import Miembro
import db
import shutil
import os
from PyQt5.QtGui import QPixmap

class EditMiembroWindow():
    def __init__(self):
        self.editar = uic.loadUi('Diseños/editMiembro.ui')
        self.startGUI()
        self.editar.show()
        
        
    def startGUI(self):
        self.editar.searchButton.clicked.connect(self.llenarCampos)
        self.editar.saveButton.clicked.connect(self.editarMiembro)
        self.editar.cancelButton.clicked.connect(self.editar.close)
        self.editar.PhotoButton.clicked.connect(self.buscarFoto)
        
    def llenarCampos(self):
        #Obtener el ID del Campo IDTXT
        id = self.editar.IDTXT.text()
        #Buscar el miembro con el ID
        miembro = db.session.query(Miembro).filter(Miembro.id == id).first()
        #Si el miembro existe, llenar los campos
        if miembro:
            self.editar.nombreTXT.setText(miembro.nombre)
            self.editar.apellidoPTXT.setText(miembro.apellidoPaterno)
            self.editar.apellidoMTXT.setText(miembro.apellidoMaterno)
            self.editar.nacimientoDate.setDate(miembro.fechaNacimiento)
            self.editar.lugarNacimientoTXT.setText(miembro.lugarDeNacimiento)
            self.editar.direccionTXT.setText(miembro.direccion)
            self.editar.estudiosCombo.setCurrentText(miembro.gradoEstudios)
            self.editar.lugarTrabajoTXT.setText(miembro.lugarTrabajo)
            self.editar.direccionTrabajoTXT.setText(miembro.domicilioTrabajo)
            self.editar.horarioTrabajoTXT.setText(miembro.horarioTrabajo)
            self.editar.civilCombo.setCurrentText(miembro.estadoCivil)
            self.editar.ocupacionTXT.setText(miembro.ocupacion)
            #Dividir Oracion en Dia y Hora
            self.editar.oracionCombo.setCurrentText(str(miembro.oracion).split(' ')[0])
            #Si mimbro.fechaDeBautismo es None,Poner la fecha actual
            if miembro.fechaDeBautismo == None:
                self.editar.dateBautismo.setDate(datetime.datetime.now())
            else:
                self.editar.dateBautismo.setDate(miembro.fechaDeBautismo)
            self.editar.lugarBauTXT.setText(miembro.lugarDeBautismo)
            if miembro.fechaDeEspirituSanto == None:
                self.editar.dateEspiritu.setDate(datetime.datetime.now())
            else:
                self.editar.dateEspiritu.setDate(miembro.fechaDeEspirituSanto)
            self.editar.lugarEspTXT.setText(miembro.lugarDeEspirituSanto)
        else:
            QMessageBox.warning(self.editar, 'Error', 'No se encontraron resultados')
            
    def editarMiembro(self):
        #Obtener el ID del Campo IDTXT
        id = self.editar.IDTXT.text()
        #Buscar el miembro con el ID
        miembro = db.session.query(Miembro).filter(Miembro.id == id).first()
        #Si el miembro existe, llenar los campos
        if miembro:
            miembro.nombre = self.editar.nombreTXT.text()
            miembro.apellidoPaterno = self.editar.apellidoPTXT.text()
            miembro.apellidoMaterno = self.editar.apellidoMTXT.text()
            miembro.fechaNacimiento = self.editar.nacimientoDate.date().toPyDate()
            miembro.lugarDeNacimiento = self.editar.lugarNacimientoTXT.text()
            miembro.direccion = self.editar.direccionTXT.text()
            miembro.gradoEstudios = self.editar.estudiosCombo.currentText()
            miembro.lugarTrabajo = self.editar.lugarTrabajoTXT.text()
            miembro.domicilioTrabajo = self.editar.direccionTrabajoTXT.text()
            miembro.horarioTrabajo = self.editar.horarioTrabajoTXT.text()
            miembro.estadoCivil = self.editar.civilCombo.currentText()
            miembro.ocupacion = self.editar.ocupacionTXT.text()
            miembro.oracion = self.editar.oracionCombo.currentText() + ' ' + str(self.editar.timeOracion.time().toString())
            miembro.fechaDeBautismo = self.editar.dateBautismo.date().toPyDate()
            miembro.lugarDeBautismo = self.editar.lugarBauTXT.text()
            miembro.fechaDeEspirituSanto = self.editar.dateEspiritu.date().toPyDate()
            miembro.lugarDeEspirituSanto = self.editar.lugarEspTXT.text()
            
            
            db.session.commit()
            QMessageBox.information(self.editar, 'Éxito', 'Miembro actualizado correctamente')
        else:
            QMessageBox.warning(self.editar, 'Error', 'No se encontraron resultados')
            
    def buscarFoto(self):
        #Obtener el ID del Campo IDTXT
        id = self.editar.IDTXT.text()
        #Buscar el miembro con el ID
        miembro = db.session.query(Miembro).filter(Miembro.id == id).first()
        #Si el miembro existe, llenar los campos
        if miembro:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.editar, 'Seleccionar Imagen', '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
            if fileName:
                #Copiar la imagen al directorio de imagenes ,si no existe, crearlo
               
                if not os.path.exists('images'):
                    os.makedirs('images')
                shutil.copy(fileName, 'images')
                miembro.fotografia = fileName
                db.session.commit()
                QMessageBox.information(self.editar, 'Éxito', 'Imagen guardada correctamente')
                #Cargar la imagen en el GraphicsView
                
                pixmap = QPixmap(miembro.fotografia)
                self.editar.Foto.setPixmap(pixmap)
        else:
            QMessageBox.warning(self.editar, 'Error', 'No se encontraron resultados')
            
            