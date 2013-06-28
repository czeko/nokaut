from lib import nokaut__api
from lib import PusteError
import sys


def main():
    if 4 == len(sys.argv):
        try:
            return nokaut__api(sys.argv[2], sys.argv[3])
        except PusteError as e:
            print e
    else:
        return 'Podaj 3 argumenty'
