from lib import nokaut_api
from lib import PusteError
import sys

def main():
	if (len(sys.argv)==4):
		try:
			print nokaut_api(sys.argv[2],sys.argv[3])
		except PusteError as e:
			print e
	else:
			return "Podaj 3 argumenty"

