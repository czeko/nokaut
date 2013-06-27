import unittest
import sys
from nokaut.lib import nokaut_api
from nokaut.lib import PusteError

class MyTest(unittest.TestCase):

    def test_czy_nie_ma(self):
        self.assertRaises(PusteError,nokaut_api,'a8839b1180ea00fa1cf7c6b74ca01bb5', 'mamamamamamama')

if __name__=="__main__":
    unittest.main()