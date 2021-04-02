import unittest
from test import hola

class checar(unittest.TestCase):
    def test_hola(self):
        b = hola("Lola", 18)
        self.assertEqual(b, "hola mi nombre es Lola y tengo 18 y me gusta la pizza")

if __name__ == "__main__":
    unittest.main()