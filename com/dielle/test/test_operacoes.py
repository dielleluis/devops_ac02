import unittest
from com.dielle.operacoes import Operacoes


class TestOperacoes(unittest.TestCase):

    def setUp(self):
        self.operacoes = Operacoes()

    def test_pow(self):
        self.assertEqual(self.operacoes.pow(2, 3), 8, 'Should be 8')


    if __name__ == '__main__':
        unittest.main()