import unittest
import main as principal

#Hacer pruebas unitarias mandando el numero de paises para crear la tabla

class TestUtils(unittest.TestCase):
    def test1(self):
        self.assertTrue(principal.tableCountries(1))                    #Hacer prueba con 1 pais
        self.assertTrue(principal.tableCountries(70))                   #Hacer prueba con 70 paises
        self.assertTrue(principal.tableCountries())                     #Hacer prueba con todos los paises
        self.assertTrue(principal.tableCountries(-1))                   #Hacer prueba con todos los paises
        self.assertTrue(principal.tableCountries("weqw"))               #Hacer prueba con todos los paises


if __name__ == '__main__':
    unittest.main()
