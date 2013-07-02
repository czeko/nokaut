from lib import nokaut_api
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
    try:
        price, url = nokaut_api(args[0],args[1])
    except IndexError:
        print 'Nokaut takes exactly 2 argument!'
    except NokautError as e:
        print e
    except Exception as e:
        print e
    else:
        return 'Price : %d, Url: %s' % (price, url)


