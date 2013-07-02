from lib import nokaut__api
from lib import PusteError
import sys
import argparse
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-k",
                  action="store_false", default=True,
                  help="key")
(options, args) = parser.parse_args()

def main():
    if 2 == len(args):
        try:
            cena, url = nokaut__api(args[0],args[1])
        except PusteError as e:
            print e
        else:
            return 'Cena: %d, Url: %s' % (cena, url)
    else:
        return 'Podaj 2 klucze'

