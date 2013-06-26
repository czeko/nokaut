from lib import nokaut_api
import getopt
import sys

def main():
	try:
		return nokaut_api(sys.argv[2],sys.argv[3])
	except IndexError:
		print "Za malo argumentow"

