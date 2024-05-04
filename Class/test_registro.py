import unittest
from unittest.mock import MagicMock
from registro import RegistroWindow as Registro

class RegistroTests(unittest.TestCase):
    def setUp(self):
        self.registro = Registro()
        self.registro.nombreTxt = MagicMock()
        self.registro.apellido1Txt = MagicMock()
        self.registro.apellido2Txt = MagicMock()
        self.registro.birthDate = MagicMock()
        self.registro.generoCombo = MagicMock()
        self.registro.telTxt = MagicMock()
        self.registro.direccTxt = MagicMock()
        self.registro.estudiosCombo = MagicMock()
        self.registro.ocupaTxt = MagicMock()
        self.registro.registerButton = MagicMock()
        self.registro.close = MagicMock()

    def test_guardar_valid_input(self):
        # Set up mock values for input fields
        self.registro.nombreTxt.text.return_value = 'John'
        self.registro.apellido1Txt.text.return_value = 'Doe'
        self.registro.apellido2Txt.text.return_value = 'Smith'
        self.registro.birthDate.date.return_value.toString.return_value = '01/01/2000'
        self.registro.generoCombo.currentText.return_value = 'Male'
        self.registro.telTxt.text.return_value = '1234567890'
        self.registro.direccTxt.text.return_value = '123 Main St'
        self.registro.estudiosCombo.currentText.return_value = 'Bachelor'
        self.registro.ocupaTxt.text.return_value = 'Engineer'

        # Call the guardar method
        self.registro.guardar()

        # Assert that the appropriate methods were called
        self.registro.registerButton.setEnabled.assert_called_once_with(False)
        self.registro.close.assert_called_once_with()

    def test_guardar_empty_fields(self):
        # Set up mock values for input fields
        self.registro.nombreTxt.text.return_value = ''
        self.registro.apellido1Txt.text.return_value = ''
        self.registro.apellido2Txt.text.return_value = ''
        self.registro.birthDate.date.return_value.toString.return_value = ''
        self.registro.generoCombo.currentText.return_value = ''
        self.registro.telTxt.text.return_value = ''
        self.registro.direccTxt.text.return_value = ''
        self.registro.estudiosCombo.currentText.return_value = ''
        self.registro.ocupaTxt.text.return_value = ''

        # Call the guardar method
        self.registro.guardar()

        # Assert that the appropriate methods were called
        self.registro.registerButton.setEnabled.assert_called_once_with(True)

if __name__ == '__main__':
    unittest.main()