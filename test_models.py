
import unittest
from models import User, Miembro

class UserTests(unittest.TestCase):
    def test_user_creation(self):
        user = User(username='john', password='password123')
        self.assertEqual(user.username, 'john')
        self.assertEqual(user.password, 'password123')

    def test_user_id(self):
        user = User(username='john', password='password123')
        self.assertIsNone(user.id)

class MiembroTests(unittest.TestCase):
    def test_miembro_creation(self):
        miembro = Miembro(
            nombre='John',
            apellidoPaterno='Doe',
            apellidoMaterno='Smith',
            fechaNacimiento='1990-01-01',
            lugarDeNacimiento='New York',
            sexo='Male',
            telefono='1234567890',
            correo='john.doe@example.com',
            direccion='123 Main St',
            gradoEstudios='Bachelor',
            ocupacion='Engineer',
            lugarTrabajo='ABC Company',
            domicilioTrabajo='456 Elm St',
            estadoCivil='Single'
        )
        self.assertEqual(miembro.nombre, 'John')
        self.assertEqual(miembro.apellidoPaterno, 'Doe')
        self.assertEqual(miembro.apellidoMaterno, 'Smith')
        self.assertEqual(miembro.fechaNacimiento, '1990-01-01')
        self.assertEqual(miembro.lugarDeNacimiento, 'New York')
        self.assertEqual(miembro.sexo, 'Male')
        self.assertEqual(miembro.telefono, '1234567890')
        self.assertEqual(miembro.correo, 'john.doe@example.com')
        self.assertEqual(miembro.direccion, '123 Main St')
        self.assertEqual(miembro.gradoEstudios, 'Bachelor')
        self.assertEqual(miembro.ocupacion, 'Engineer')
        self.assertEqual(miembro.lugarTrabajo, 'ABC Company')
        self.assertEqual(miembro.domicilioTrabajo, '456 Elm St')
        self.assertEqual(miembro.estadoCivil, 'Single')

if __name__ == '__main__':
    unittest.main()