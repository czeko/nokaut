import unittest
import sys
from nokaut.script import main


class MyTest(unittest.TestCase):
	def test_ilosc_arg(self):
		self.assertEqual(main(),"Podaj 3 argumenty")


if __name__=="__main__":
 	unittest.main()