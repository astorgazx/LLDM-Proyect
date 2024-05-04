from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import QMessageBox

from models import Miembro
import datetime

import db


class RegistroWindow():
    def __init__(self):
        self.registro = uic.loadUi('Diseños/registroM.ui')
        self.startGUI()
        self.registro.show()
        
        
        
    def startGUI(self):
        self.registro.registerButton.clicked.connect(self.guardar)
        self.registro.cancelButton.clicked.connect(self.registro.close)
        
        #Si el la checkbox de trabajo esta seleccionada, habilitar los campos de trabajo
        self.registro.trabajaCheckBox.stateChanged.connect(self.habilitarCamposTrabajo)
        
    def habilitarCamposTrabajo(self):
        if self.registro.trabajaCheckBox.isChecked():
            self.registro.label_13.setEnabled(True)
            self.registro.lugarTrabajoTxt.setEnabled(True)
            self.registro.label_14.setEnabled(True)
            self.registro.direccionTrabajoTxt.setEnabled(True)
            self.registro.label_15.setEnabled(True)
            self.registro.horarioTrabajoTxt.setEnabled(True)
        else:
            self.registro.label_13.setEnabled(False)
            self.registro.lugarTrabajoTxt.setEnabled(False)
            self.registro.label_14.setEnabled(False)
            self.registro.direccionTrabajoTxt.setEnabled(False)
            self.registro.label_15.setEnabled(False)
            self.registro.horarioTrabajoTxt.setEnabled(False)
        
    def guardar(self):
        #Verificar que los campos no estén vacíos y que coincidan con el Modelo Miembro
        nombre = self.registro.nombreTxt.text().capitalize()
        apellidoPaterno = self.registro.apellido1Txt.text().capitalize()
        apellidoMaterno = self.registro.apellido2Txt.text().capitalize()
        fechaNacimiento = datetime.datetime.strptime(self.registro.birthDate.date().toString('dd/MM/yyyy'), '%d/%m/%Y').date()
        sexo = self.registro.generoCombo.currentText()
        telefono = self.registro.telTxt.text()
        direccion = self.registro.direccTxt.text()
        estudios = self.registro.estudiosCombo.currentText()
        ocupacion = self.registro.ocupaTxt.text()
        estadoCivil = self.registro.estadoCivilCombo.currentText()
        
        contaador = 0
        
        
        
        
        if '' not in [nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, telefono, direccion, estudios, ocupacion]:
            
            if self.registro.trabajaCheckBox.isChecked():
                lugarTrabajo = self.registro.lugarTrabajoTxt.text()
                domicilioTrabajo = self.registro.direccionTrabajoTxt.text()
                horarioTrabajo = self.registro.horarioTrabajoTxt.text()
            try:
                
                #Verificar cuantas veces entra al metodo
                contaador = contaador + 1
                print(contaador)
                # Deshabilitar el botón de registro para evitar doble clic
                
                self.registro.registerButton.setEnabled(False)
                
                #Agregar una validación para que no se pueda registrar un miembro con el mismo nombre apellido y fecha de nacimiento
                miembro = db.session.query(Miembro).filter(Miembro.nombre == nombre, Miembro.apellidoPaterno == apellidoPaterno, Miembro.apellidoMaterno == apellidoMaterno, Miembro.fechaNacimiento == fechaNacimiento).first()
                if miembro:
                    QMessageBox.warning(self.registro, 'Error', 'Ya existe un miembro con el mismo nombre, apellido y fecha de nacimiento')
                    self.registro.registerButton.setEnabled(True)
                    return
                

                # Crear un objeto de tipo Miembro
                miembro = Miembro(nombre=nombre, apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno, fechaNacimiento=fechaNacimiento, sexo=sexo, telefono=telefono, direccion=direccion, gradoEstudios=estudios, ocupacion=ocupacion, estadoCivil=estadoCivil, lugarTrabajo=lugarTrabajo, domicilioTrabajo=domicilioTrabajo, horarioTrabajo=horarioTrabajo)
                # Guardar el objeto en la base de datos
                db.session.add(miembro)
                db.session.commit()
                db.session.close()
                
                QMessageBox.information(self.registro,"Informacion","Se agrego correctamente")

                
                self.registro.close()
            except Exception as e:
                # Handle the exception here
                print(e)
                # Habilitar el botón de registro en caso de error
                self.registro.registerButton.setEnabled(True)

                QMessageBox.warning(self.registro, 'Error', 'Ocurrió un error al registrar el miembro')
                # Imprimir el error en la consola
                print(e)
        else:
            QMessageBox.about(self.registro, 'Error', 'Todos los campos son obligatorios')
                
            