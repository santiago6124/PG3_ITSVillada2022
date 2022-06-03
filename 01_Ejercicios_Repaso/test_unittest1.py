import ej1BuscarAdentroSantiagoCarranza  # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(ej1BuscarAdentroSantiagoCarranza.funcion(['8', '12', '9', '45']), ['4','8', '12', '9', '45'])

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 4)

if __name__ == '__main__':
    unittest.main()
