from Class.mainWindow import MainWindow
import db
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from models import User


class Login():
    def __init__(self): # Constructor de la clase
        self.login = uic.loadUi('Diseños/login.ui') # Cargar el archivo .ui de la carpeta de Diseños
        self.startGUI() # Iniciar la interfaz gráfica
        self.login.show() # Muestra el dialog
        

    def ingresar(self):
        #Usar la clase User de models para verificar si el usuario y contraseña son correctos
    
        username = self.login.userText.text()
        password = self.login.passText.text()
        
        user = db.session.query(User).filter(User.username == username, User.password == password).first()
        
        if username == '' or password == '':
            QMessageBox.about(self.login, 'Error', 'Todos los campos son obligatorios')
            self.login.userText.setFocus()    
            
        
        if user:
            QMessageBox.about(self.login, 'Bienvenido', 'Usuario y contraseña correctos')
            #Abrir la ventana principal
            self.login.close()
            self.mainWindow = MainWindow()
        else:
            QMessageBox.about(self.login, 'Error', 'Usuario o contraseña incorrectos')
        
        
    def startGUI(self):
        self.login.loginButton.clicked.connect(self.ingresar)
        