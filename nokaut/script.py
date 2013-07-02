from lib import nokaut__api
from lib import NokautError
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
            price, url = nokaut__api(args[0],args[1])
        except NokautError as e:
            print e
        except Exception as e:
            print e
        else:
            return 'Price : %d, Url: %s' % (price, url)
    else:
        return 'Nokaut takes exactly 2 arguments!'

