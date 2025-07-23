# Se importa el modulo para crear pruebas
import unittest
# Se importa las funciones del archivo 'calculadora.py' para probar
from calculadora import suma, resta, multi, divi

# Se crea una clase de pruebas que hereda de unittest.TestCase
class TestCalculadora(unittest.TestCase):
    
    # Un metodo para probar la funcion suma
    def test_suma(self):
        # Se verifica que 5 + 3 sean 8
        self.assertEqual(suma(5, 3), 8)
        # Se verifica que 10 + 500 sean 510
        self.assertEqual(suma(10, 500), 510)
    
    # Y asi para los demas metodos
    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(-1, 20), -21)
        
    def test_multi(self):
        self.assertEqual(multi(5, 5), 25)
        self.assertEqual(multi(10, 500), 5000)
        
    
    def test_multi(self):
        self.assertEqual(divi(5, 5), 1)
        # Se verifica que al dividir entre 0 se lance el error
        with self.assertRaises(ValueError):
            divi(5, 0)

# Si se ejecuta el codigo directamente se corren las pruebas
if __name__ == '__main__':
    unittest.main()